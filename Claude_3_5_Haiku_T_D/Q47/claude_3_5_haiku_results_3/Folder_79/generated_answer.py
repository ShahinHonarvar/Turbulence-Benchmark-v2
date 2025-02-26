def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(3, 5):
        for start in range(1, 10 - length + 1):
            substring = s[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result