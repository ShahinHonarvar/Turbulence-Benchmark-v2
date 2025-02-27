def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[3:10].lower()
    substring_set = set(substring)
    if substring_set.issubset(english_letters):
        for i in range(5, len(substring) + 1):
            for j in range(len(substring) - i + 1):
                if substring[j:j + i] == substring[j:j + i][::-1]:
                    palindromes.add(substring[j:j + i])
    return palindromes