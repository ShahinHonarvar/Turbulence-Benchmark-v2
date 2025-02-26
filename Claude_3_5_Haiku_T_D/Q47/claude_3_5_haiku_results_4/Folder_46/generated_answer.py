def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_palindromes = set()
    for start in range(11, 98):
        for length in range(29, 63):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                valid_palindromes.add(substring)
    return valid_palindromes