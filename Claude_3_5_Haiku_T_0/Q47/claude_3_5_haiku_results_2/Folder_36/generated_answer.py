def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[124:284].lower()
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes