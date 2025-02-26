def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[32:80].lower()
    for length in range(35, 42):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes