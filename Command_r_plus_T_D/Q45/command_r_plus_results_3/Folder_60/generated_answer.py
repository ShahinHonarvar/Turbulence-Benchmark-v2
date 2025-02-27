def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join(filter(english_letters.__contains__, s[3:7]))
    sub_str_len = len(sub_str)
    palindromes = set()
    for i in range(sub_str_len // 2 + 1):
        for j in range(sub_str_len - i + 1):
            window = sub_str[j:j + i]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes