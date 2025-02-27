def palindromes_of_specific_lengths(s):
    substring = s[33:86]
    length_range = range(26, 32)
    palindromes = set()
    for length in length_range:
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower() and all((char.isalpha() for char in sub)):
                palindromes.add(sub)
    return palindromes