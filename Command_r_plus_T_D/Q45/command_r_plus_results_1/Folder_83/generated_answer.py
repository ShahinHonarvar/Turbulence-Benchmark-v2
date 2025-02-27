def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    substring = s[2:10].lower()
    for i in range(len(substring)):
        for j in range(i + 6, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1] and set(substring[i:j]).issubset(english_letters):
                palindromes.add(substring[i:j])
    return palindromes