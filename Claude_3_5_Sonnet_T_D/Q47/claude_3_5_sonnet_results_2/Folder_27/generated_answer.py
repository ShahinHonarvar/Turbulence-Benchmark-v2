def palindromes_of_specific_lengths(s):
    result = set()
    s = s[13:100].upper()
    for i in range(len(s)):
        for length in range(26, 30):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring.lower())
    return result