def palindromes_of_specific_lengths(s):
    s = s[23:85]
    palindromes = set()
    for length in range(21, 32):
        for start_index in range(len(s) - length + 1):
            substring = s[start_index:start_index + length]
            if all((letter.isalpha() or not letter.isalpha() for letter in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes