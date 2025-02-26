def palindromes_of_specific_lengths(s):
    result = set()
    for start in range(18, 89 - 11):
        for length in range(12, 15):
            substring = s[start:start + length].lower()
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result