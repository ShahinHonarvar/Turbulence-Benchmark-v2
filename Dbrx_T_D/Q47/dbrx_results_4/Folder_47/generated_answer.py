def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for length in range(14, 53):
        for start_index in range(39, len(s) - length + 2):
            substring = s[start_index:start_index + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                valid_palindromes.add(substring)
    return valid_palindromes