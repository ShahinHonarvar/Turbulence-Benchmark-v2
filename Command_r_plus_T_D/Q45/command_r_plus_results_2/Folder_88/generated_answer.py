def palindromes_between_indices(s):
    sub_str = s[3:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    palindromes = set()
    for i in range(len(filtered_sub_str) - 5):
        for j in range(i + 1, len(filtered_sub_str) - i):
            window = filtered_sub_str[i:j]
            if window == window[::-1] and len(window) >= 6:
                palindromes.add(window)
    return palindromes