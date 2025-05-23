def palindromes_of_specific_lengths(s):
    substring = s[23:83].lower()
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes