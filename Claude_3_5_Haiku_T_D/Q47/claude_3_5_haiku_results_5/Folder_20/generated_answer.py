def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[20:75].lower()
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes