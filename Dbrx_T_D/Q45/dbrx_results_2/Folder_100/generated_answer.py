def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(0, 6):
        for j in range(i, 6):
            substring = s[i:j + 1]
            if set(substring).issubset(english_letters):
                reversed_substring = substring[::-1]
                if substring.lower() == reversed_substring.lower() and len(substring) >= 6:
                    palindromes.add(substring)
    return palindromes