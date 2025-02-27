def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    result = set()
    for i in range(len(s)):
        for j in range(43, 48):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result