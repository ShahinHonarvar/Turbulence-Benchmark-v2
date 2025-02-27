def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    candidates = set(s)
    palindromes = set()
    for candidate in candidates:
        if len(candidate) >= 51 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes