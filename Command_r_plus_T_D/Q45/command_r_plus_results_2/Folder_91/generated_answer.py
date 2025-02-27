def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    substring = s[2:7]
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(3, len(substring) + 1):
            for j in range(len(substring) - i + 1):
                if substring[j:j + i] == substring[j:j + i][::-1]:
                    palindromes.add(substring[j:j + i])
    return palindromes