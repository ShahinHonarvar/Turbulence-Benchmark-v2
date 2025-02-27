def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(8):
        for j in range(4, 6):
            if i + j <= 8:
                substring = s[i:i + j].lower()
                if substring and all((c in english_letters for c in substring)) and (substring[0] == substring[-1]) and (substring[1::2] == substring[1::2][::-1]):
                    palindromes.add(''.join(substring))
    return palindromes