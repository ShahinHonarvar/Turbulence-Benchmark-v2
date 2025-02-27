def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[14:73].lower()
    for length in range(19, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes