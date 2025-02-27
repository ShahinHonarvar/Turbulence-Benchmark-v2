def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[26:78].lower()
    for i in range(len(substring) - 17):
        for j in range(2):
            candidate = substring[i:i + 18 + j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes