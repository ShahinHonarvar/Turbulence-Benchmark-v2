def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    valid_palindromes = set()
    for length in range(3, 6):
        for start in range(7 - length):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes