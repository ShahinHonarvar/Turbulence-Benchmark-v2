def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_palindromes = set()
    for length in range(10, 51):
        for start in range(10, 101 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes