def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(63, 71):
        for length in range(4, 6):
            if i + length <= len(s):
                pal = s[i:i + length].lower()
                if pal == pal[::-1]:
                    palindromes.add(pal)
    return palindromes