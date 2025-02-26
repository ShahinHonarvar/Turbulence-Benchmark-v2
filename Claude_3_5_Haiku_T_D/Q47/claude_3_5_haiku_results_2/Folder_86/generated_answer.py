def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[30:96].lower()
    for length in range(34, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) != length:
                continue
            if all((c.isalpha() for c in candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes