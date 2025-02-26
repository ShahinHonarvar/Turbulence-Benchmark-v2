def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:71].lower()
    for i in range(len(s)):
        for j in range(i + 24, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result