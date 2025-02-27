def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[119:257]
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes