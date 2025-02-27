def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[16:73].lower()
    palindromes = set()
    for i in range(len(substring) - 50):
        for j in range(2):
            candidate = substring[i:i + 50 + j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes