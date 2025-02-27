def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[35:93].lower()
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes