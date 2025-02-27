def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    valid_palindromes = set()
    for length in range(4, 6):
        for start in range(8 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes