def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[14:91]
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes