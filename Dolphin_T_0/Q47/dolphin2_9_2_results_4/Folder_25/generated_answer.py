def palindromes_of_specific_lengths(s):
    substring = s[26:85]
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(substring) - length + 1):
            sub_pal = substring[i:i + length]
            if all((c.isalpha() for c in sub_pal)):
                if sub_pal.lower() == sub_pal.lower()[::-1]:
                    palindromes.add(sub_pal.lower())
    return palindromes