def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[6:10].lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i, len(substr)):
            substr_part = substr[i:j + 1]
            if set(substr_part).issubset(english_letters):
                if substr_part == substr_part[::-1]:
                    palindromes.add(substr_part)
    return {p for p in palindromes if len(p) >= 3}