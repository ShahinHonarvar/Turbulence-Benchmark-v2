def palindromes_between_indices(s):
    sub_str = s[6:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join(filter(english_letters.__contains__, sub_str))
    palindromes = set()
    for i in range(len(filtered_sub_str) - 3 + 1):
        window = filtered_sub_str[i:i + 4]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes