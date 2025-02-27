def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join(filter(english_letters.__contains__, s[1:5]))
    return set((word for word in sub_str if len(word) >= 4 and word == word[::-1]))