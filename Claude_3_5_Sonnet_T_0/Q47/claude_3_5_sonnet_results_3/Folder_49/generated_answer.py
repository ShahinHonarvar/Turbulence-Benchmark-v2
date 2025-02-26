def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:101].lower()
    for i in range(len(s)):
        for j in range(i + 10, min(i + 51, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result