def palindromes_of_specific_lengths(s):
    if len(s) < 91:
        return set()
    substring = s[26:91].lower()
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes