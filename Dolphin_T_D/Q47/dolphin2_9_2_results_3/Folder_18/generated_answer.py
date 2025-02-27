def palindromes_of_specific_lengths(s):
    s_substring = s[10:84]
    result = set()
    for i in range(13, 67):
        for j in range(len(s_substring) - i + 1):
            substring = s_substring[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result