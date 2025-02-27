def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[2:6].lower()
    english_letters_in_s = set(s_lower) & english_letters
    s_lower_english_letters_only = ''.join(sorted(s_lower))
    palindromes = set()
    for i in range(len(s_lower_english_letters_only) - 4 + 1):
        window = s_lower_english_letters_only[i:i + 5]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes