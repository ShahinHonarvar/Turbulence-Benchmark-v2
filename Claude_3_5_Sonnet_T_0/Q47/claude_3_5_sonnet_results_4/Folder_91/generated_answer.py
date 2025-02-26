def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:11].lower()
    for i in range(11):
        for j in range(i + 3, min(i + 6, 12)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result