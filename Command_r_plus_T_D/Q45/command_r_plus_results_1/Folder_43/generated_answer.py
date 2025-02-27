def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    sub_str = s[2:6].lower()
    for char in sub_str:
        if char in english_letters:
            english_letters.remove(char)
    sub_str = ''.join(sorted(sub_str))
    for i in range(len(sub_str) - 3 + 1):
        window = sub_str[i:i + 4]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes