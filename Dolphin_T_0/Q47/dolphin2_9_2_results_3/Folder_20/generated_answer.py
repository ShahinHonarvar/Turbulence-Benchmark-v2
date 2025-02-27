def palindromes_of_specific_lengths(s):
    s = s[20:75]
    result = set()
    for i in range(36, 43):
        for j in range(0, len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and all((c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in sub)):
                result.add(sub)
    return result