def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    if len(s) < 98:
        return palindromes
    substring = s[24:98]
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes