def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[2:10].lower()
    filtered_letters = [c for c in s_lower if c in english_letters]
    palindromes = set()
    for i in range(len(filtered_letters) - 6):
        window = filtered_letters[i:i + 7]
        if window == window[::-1]:
            palindromes.add(''.join(window))
    return palindromes