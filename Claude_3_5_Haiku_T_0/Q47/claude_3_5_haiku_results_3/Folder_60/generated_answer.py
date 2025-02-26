def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[23:83].lower()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes