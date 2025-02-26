def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_palindromes = set()
    if len(s) < 289:
        return valid_palindromes
    substring = s[127:289]
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    valid_palindromes.add(candidate)
    return valid_palindromes