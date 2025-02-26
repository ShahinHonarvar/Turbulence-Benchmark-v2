def palindromes_of_specific_lengths(s):
    if len(s) < 8:
        return set()
    palindromes = set()
    substring = s[1:8].lower()
    for length in range(3, 5):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes