def palindromes_of_specific_lengths(s):
    s = s[14:86]
    result = set()
    for i in range(50, 61):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                result.add(s[j:j + i].lower())
    return result