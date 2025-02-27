def palindromes_of_specific_lengths(s):
    s = s[127:289]
    palindromes = set()
    for length in range(119, 142):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes