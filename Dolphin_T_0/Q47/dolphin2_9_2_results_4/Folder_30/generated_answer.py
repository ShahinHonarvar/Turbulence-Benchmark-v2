def palindromes_of_specific_lengths(s):
    s = s[13:91]
    lengths = [i for i in range(55, 72)]
    palindromes = set()
    for length in lengths:
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindrome = ''.join((c for c in substring if c.isalpha()))
                if palindrome.lower() == palindrome.lower()[::-1]:
                    palindromes.add(palindrome)
    return palindromes