def palindromes_of_specific_lengths(s):
    result = set()
    s = s[3:301].lower()
    for i in range(len(s)):
        for j in range(i + 30, min(i + 301, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result