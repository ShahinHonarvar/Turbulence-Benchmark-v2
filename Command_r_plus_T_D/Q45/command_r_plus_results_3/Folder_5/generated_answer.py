def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join((c for c in s[4:9] if c in english_letters))
    sub_str = sub_str.lower()
    return {sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 4, len(sub_str) + 1) if sub_str[i:j] == sub_str[i:j][::-1]}