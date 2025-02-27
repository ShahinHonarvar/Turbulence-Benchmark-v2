def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, 7):
        for j in range(i + 1, 7):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and set(substring.lower()).issubset(english_letters):
                palindromes.add(substring)
    return palindromes