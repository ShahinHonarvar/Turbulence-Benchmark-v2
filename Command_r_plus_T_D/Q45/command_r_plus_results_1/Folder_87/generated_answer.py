def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    substring = s[3:10]
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(3, len(substring)):
            for j in range(i + 3, len(substring) + 1):
                sub = substring[i:j]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes