def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[2:6].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] in english_letters and s[j] in english_letters:
                substring = s[i:j + 1]
                if substring == substring[::-1] and len(substring) >= 5:
                    palindromes.add(substring)
    return palindromes