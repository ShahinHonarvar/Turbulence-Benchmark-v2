def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join(filter(english_letters.__contains__, s[3:9]))
    return set((sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 4, len(sub_str) + 1) if sub_str[i:j] == sub_str[i:j][::-1]))