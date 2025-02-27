def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(100, 301):
        for j in range(i + 50, min(i + 101, 301)):
            sub_string = s[i:j]
            Cleaned_sub_string = ''.join((c for c in sub_string if c.isalpha()))
            Cleaned_sub_string = Cleaned_sub_string.lower()
            if Cleaned_sub_string == Cleaned_sub_string[::-1]:
                palindromes.add(Cleaned_sub_string)
    return palindromes