def palindromes_of_specific_lengths(s):
    s = s[130:296]
    set_palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((char.isalpha() for char in substring)) and substring.lower() == substring.lower()[::-1]:
                set_palindromes.add(substring)
    return set_palindromes