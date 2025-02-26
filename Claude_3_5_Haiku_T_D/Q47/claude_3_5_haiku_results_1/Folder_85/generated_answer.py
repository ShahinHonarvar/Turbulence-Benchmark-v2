def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(6, 10):
        for start in range(29, 99 - length + 1):
            substring = s[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result