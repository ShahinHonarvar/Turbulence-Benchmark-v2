def palindromes_of_specific_lengths(s):
    s = s[17:99]
    palindromes = set()
    for i in range(18, len(s) - 30):
        for j in range(4, 52):
            substring = s[i:i + j]
            if set(substring.lower()) <= set('abcdefghijklmnopqrstuvwxyz'):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes