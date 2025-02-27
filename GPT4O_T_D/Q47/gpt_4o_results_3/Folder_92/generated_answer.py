def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    valid_palindromes = set()
    for start in range(3):
        for length in range(3, 5):
            substring = s[start:start + length]
            if len(substring) == length and substring.isalpha() and (substring == substring[::-1]):
                valid_palindromes.add(substring)
    return valid_palindromes