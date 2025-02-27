def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(0, min(11, len(s))):
        for j in range(3, 6):
            if i + j <= len(s):
                substring = s[i:i + j].lower()
                if substring[0] in english_letters and all((char in english_letters for char in substring)) and (substring[0] == substring[-1]) and (substring[1:-1] == substring[1:-1][::-1]):
                    palindromes.add(substring)
    return palindromes