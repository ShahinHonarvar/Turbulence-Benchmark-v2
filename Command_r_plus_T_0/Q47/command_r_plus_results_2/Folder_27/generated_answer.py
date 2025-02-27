def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[12:100].lower()
    for i in range(len(substring) - 25):
        for length in range(26, 30):
            if length + i > len(substring):
                break
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes