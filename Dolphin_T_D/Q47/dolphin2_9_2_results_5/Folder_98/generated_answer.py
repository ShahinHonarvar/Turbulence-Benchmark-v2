def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[:21]
    palindromes = set()
    for length in range(5, 81):
        for i in range(len(substring) - length + 1):
            fragment = substring[i:i + length]
            if fragment == fragment[::-1] and all((char.isalpha() for char in fragment)):
                palindromes.add(fragment)
    return palindromes