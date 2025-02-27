def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[2:10].lower()
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(3, 7):
            for j in range(len(substring) - i + 1):
                sub = substring[j:j + i]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes