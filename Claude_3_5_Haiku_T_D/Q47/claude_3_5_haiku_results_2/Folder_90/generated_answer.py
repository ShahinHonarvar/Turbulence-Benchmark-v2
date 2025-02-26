def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_palindromes = set()
    for start in range(106, 281 - 135):
        for length in range(136, 152):
            substring = s[start:start + length]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes