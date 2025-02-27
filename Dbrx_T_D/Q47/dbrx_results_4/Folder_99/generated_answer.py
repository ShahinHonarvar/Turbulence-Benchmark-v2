def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(127, 289):
        for length in range(119, 142):
            substring = s[i:i + length].lower()
            if len(s) == length and all((c in english_letters for c in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes