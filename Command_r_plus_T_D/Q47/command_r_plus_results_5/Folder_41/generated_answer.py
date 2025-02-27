def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[1:8]
    substring_lower = substring.lower()
    palindromes = set()
    for i in range(len(substring_lower)):
        for j in range(i + 3, min(i + 5, len(substring_lower) + 1)):
            substr = substring_lower[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes