def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:21].lower()
    for length in range(5, 81):
        for i in range(21 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result