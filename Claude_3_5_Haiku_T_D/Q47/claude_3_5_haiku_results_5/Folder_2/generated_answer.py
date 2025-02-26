def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for start in range(10, 60 - 17):
        for length in range(18, 37):
            substring = s[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes