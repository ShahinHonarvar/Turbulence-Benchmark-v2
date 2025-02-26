def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:5].lower()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 4, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result