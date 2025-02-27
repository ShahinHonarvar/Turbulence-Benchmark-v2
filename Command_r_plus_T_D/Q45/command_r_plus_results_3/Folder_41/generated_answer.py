def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join((c for c in s[2:4] if c in english_letters))
    return set((sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 3, len(sub_str) + 1) if sub_str[i:j] == sub_str[i:j][::-1]))