def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(14, 53):
        for i in range(39, 95 - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result