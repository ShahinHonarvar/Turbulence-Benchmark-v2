def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    english_letters_in_s = set((c.lower() for c in s if c.lower() in english_letters))
    chars_between_indices = set((s[i].lower() for i in range(min(8, len(s) - 1))))
    palindromes = set()
    for p_len in range(7, min(9, len(s)) + 1):
        for p in english_letters_in_s:
            if p in chars_between_indices:
                combinations = [p] * (p_len // 2) + [p.upper()] * (p_len // 2)
                if p_len % 2 != 0:
                    combinations.insert(p_len // 2, p)
                for c in combinations:
                    palindromes.add(c)
    return palindromes