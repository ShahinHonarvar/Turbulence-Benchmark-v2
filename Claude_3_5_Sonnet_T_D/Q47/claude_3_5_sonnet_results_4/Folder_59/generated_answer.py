def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:101].lower()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 15, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha() and (3 <= len(substring) <= 15):
                result.add(substring)
    return result