def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[5:10].lower()
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(len(substring)):
            for j in range(i + 4, len(substring) + 1):
                sub = substring[i:j]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes