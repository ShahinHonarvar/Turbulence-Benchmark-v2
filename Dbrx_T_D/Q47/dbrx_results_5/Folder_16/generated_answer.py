def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(51, 61):
        for start in range(15, len(s) - length + 1):
            substring = s[start:start + length].lower()
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes