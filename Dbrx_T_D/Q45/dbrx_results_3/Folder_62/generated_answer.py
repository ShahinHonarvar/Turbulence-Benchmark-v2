from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    chars = defaultdict(int)
    for i in range(9):
        chars[s[i]] += 1
    palindromes = set()
    for _ in range(2 ** 9):
        candidate = ''.join((k * v for k, v in chars.items()))
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            palindromes.add(candidate)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            chars[char] -= 1
            if chars[char] == 0:
                del chars[char]
            if sum(chars.values()) == 0:
                break
    return palindromes