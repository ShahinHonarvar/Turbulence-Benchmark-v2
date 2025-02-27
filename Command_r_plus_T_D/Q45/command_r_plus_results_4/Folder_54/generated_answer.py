def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    substring = s[4:10]
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(4, len(substring)):
            for j in range(i + 1, len(substring) + 1):
                sub_sub_string = substring[i:j]
                if sub_sub_string == sub_sub_string[::-1] and len(sub_sub_string) >= 4:
                    palindromes.add(sub_sub_string)
    return palindromes