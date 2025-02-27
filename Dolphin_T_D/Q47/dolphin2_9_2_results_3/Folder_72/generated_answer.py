def palindromes_of_specific_lengths(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s[25:91].lower()
    lengths = range(27, 59)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c in letters for c in substring)):
                palindromes.add(substring)
    return palindromes