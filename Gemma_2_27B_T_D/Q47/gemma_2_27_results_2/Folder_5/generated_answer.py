def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[63:71]
    for i in range(len(substring) - 4):
        for j in range(i + 4, min(len(substring), i + 6)):
            pal = substring[i:j]
            if pal.lower() == pal.lower()[::-1] and pal.isalpha():
                palindromes.add(pal)
    return palindromes