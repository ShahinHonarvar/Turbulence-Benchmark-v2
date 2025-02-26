def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[:11].lower()
    for length in range(3, 6):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate.isalpha():
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes