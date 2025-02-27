def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_str = ''.join(filter(english_letters.__contains__, s[3:8].lower()))
    return set((w for w in filtered_str if filtered_str.count(w) > 1 and len(w) >= 4))