def palindromes_of_specific_lengths(s):
    sub_string = s[30:96]
    palindromes = set()
    for length in range(34, 56):
        for start in range(0, len(sub_string) - length + 1):
            sub_pal = sub_string[start:start + length]
            if sub_pal.lower() == sub_pal.lower()[::-1] and sub_pal.isalpha():
                palindromes.add(sub_pal)
    return palindromes