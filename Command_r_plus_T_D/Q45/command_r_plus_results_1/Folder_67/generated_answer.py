def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = s[2:7]
    sub_str_set = set(sub_str)
    palindromes = set()
    if sub_str_set.issubset(english_letters):
        for i in range(3, len(sub_str) + 1):
            for j in range(len(sub_str) - i + 1):
                substring = sub_str[j:j + i]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes