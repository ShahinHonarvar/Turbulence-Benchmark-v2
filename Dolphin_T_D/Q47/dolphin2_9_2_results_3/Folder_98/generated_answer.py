def palindromes_of_specific_lengths(s: str) -> set:
    s = s[0:21].lower()
    palindromes = set()
    for i in range(len(s) - 4, -1, -1):
        for j in range(i + 5, min(i + 81, len(s)) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    if not palindromes:
        return set()
    return palindromes