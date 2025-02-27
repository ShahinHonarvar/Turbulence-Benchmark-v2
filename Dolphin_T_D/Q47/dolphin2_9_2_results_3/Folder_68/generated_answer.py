def palindromes_of_specific_lengths(s):
    s = s[:51]
    result = set()
    for i in range(50, 0, -1):
        for j in range(len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i].lower()[::-1] and s[j:j + i].isalpha():
                result.add(s[j:j + i])
    return result