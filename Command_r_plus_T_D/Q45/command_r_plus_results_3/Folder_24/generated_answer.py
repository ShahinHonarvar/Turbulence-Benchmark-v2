def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join((c for c in s[2:10] if c in english_letters))
    sub_str = sub_str.lower()
    palindromes = set()
    for i in range(4, len(sub_str) + 1):
        for j in range(len(sub_str) - i + 1):
            substring = sub_str[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes