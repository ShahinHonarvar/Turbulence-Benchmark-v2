from collections import defaultdict

def palindromes_between_indices(string):
    valid_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = set()
    if len(string) < 10:
        return result
    for i in range(0, len(string) + 1):
        if i < 7 or i > 9:
            continue
        window = string[i - 3:i + 1]
        if len(window) < 3:
            continue
        valid = all((letter in valid_letters for letter in window))
        if not valid:
            continue
        for j in range(1, len(window) // 2 + 1):
            if len(window) % 2 != 0 and j == len(window) // 2:
                continue
            if window[j - 1] != window[-j]:
                break
            if j == len(window) // 2 and window[:j] == window[j:][::-1]:
                result.add(''.join(window))
            if len(window) % 2 == 0 and j == len(window) // 2 - 1 and (window[j - 1:j + 1] == window[-j - 1:-j][::-1]):
                result.add(''.join(window))
    return result