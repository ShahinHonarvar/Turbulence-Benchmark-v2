def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for length in range(3, 61):
        for start in range(70, 141 - length):
            substring = s[start:start + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes