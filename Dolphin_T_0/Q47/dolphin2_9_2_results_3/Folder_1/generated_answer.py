def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(15, 90):
        for j in range(i + 39, i + 73):
            substring = s[i:j]
            normalized_substring = ''.join((c.lower() for c in substring if c.isalpha()))
            if normalized_substring == normalized_substring[::-1]:
                palindromes.add(normalized_substring)
    return palindromes