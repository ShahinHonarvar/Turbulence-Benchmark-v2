def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:8].lower()
    for i in range(len(s)):
        for j in range(i + 3, i + 5):
            if j <= len(s):
                substring = s[i:j]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result