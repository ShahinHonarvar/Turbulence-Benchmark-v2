def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(43, 48):
        for index in range(16, len(s) - length + 1):
            substring = s[index:index + length].lower()
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes