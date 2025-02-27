def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(3, 6):
        if s[i].lower() in english_letters:
            substring = s[3:6].lower()
            for j in range(len(substring) // 2 + 1):
                if substring[:j] == substring[-j:]:
                    palindromes.add(substring[:j])
    return palindromes