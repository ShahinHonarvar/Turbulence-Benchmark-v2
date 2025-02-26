def palindromes_of_specific_lengths(s):
    if len(s) <= 77:
        return set()
    palindromes = set()
    substring = s[23:78].lower()
    for length in range(13, 41):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes