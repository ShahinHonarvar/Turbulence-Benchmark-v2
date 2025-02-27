def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    for i in range(2, 5):
        for j in range(i + 1, 6):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes