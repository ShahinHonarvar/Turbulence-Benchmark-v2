def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) <= 74:
        return palindromes
    substring = s[20:75].lower()
    for length in range(36, 43):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes