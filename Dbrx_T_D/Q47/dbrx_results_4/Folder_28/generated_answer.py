def palindromes_of_specific_lengths(s):
    english_letters_lower = set('abcdefghijklmnopqrstuvwxyz')
    english_letters_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(32, 72):
        for j in range(21, 33):
            substring = s[i:i + j]
            if all((char in english_letters_lower or char in english_letters_upper for char in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes