def palindromes_between_indices(s):
    sub_str = s[3:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((char for char in sub_str if char in english_letters))
    palindromes = set()
    for i in range(len(filtered_sub_str) - 4):
        for j in range(i + 1, len(filtered_sub_str) - i):
            window = filtered_sub_str[i:j]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes