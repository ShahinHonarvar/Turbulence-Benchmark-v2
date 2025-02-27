def palindromes_between_indices(s):
    english_lowercase_letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(4, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if english_lowercase_letters >= set(substring) - {' ', '.', ','}:
                if substring == substring[::-1]:
                    result.add(substring)
    return result