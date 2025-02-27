def palindromes_of_specific_lengths(s):
    subset = s[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(subset) - length + 1):
            pal = subset[i:i + length].lower()
            if pal == pal[::-1]:
                if pal.isalpha():
                    palindromes.add(pal)
    return palindromes