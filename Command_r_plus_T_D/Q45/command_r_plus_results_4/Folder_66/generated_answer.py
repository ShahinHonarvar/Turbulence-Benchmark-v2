def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_lower = s[:6].lower()
    s_english_letters = ''.join((c for c in s_lower if c in english_letters))
    palindromes = set()
    for i in range(len(s_english_letters)):
        for j in range(i + 1, len(s_english_letters) + 1):
            substring = s_english_letters[i:j]
            if substring == substring[::-1] and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes