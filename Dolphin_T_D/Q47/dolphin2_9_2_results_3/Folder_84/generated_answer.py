def palindromes_of_specific_lengths(s):
    substring = s[23:78]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            pal = substring[i:i + length].lower()
            if pal == pal[::-1] and pal.isalpha():
                palindromes.add(pal)
    return palindromes