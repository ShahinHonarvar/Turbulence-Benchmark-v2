def palindromes_of_specific_lengths(s):
    result = set()
    s = s[12:57].lower()
    for i in range(len(s)):
        for j in range(i + 20, i + 22):
            if j <= len(s):
                substring = s[i:j]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result