def palindromes_of_specific_lengths(s):
    s = s[15:73]
    length_19_55 = [i for i in range(19, 56)]
    palindromes = set()
    for length in length_19_55:
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                clean_substring = ''.join((e for e in substring if e.isalpha()))
                if len(clean_substring) in length_19_55:
                    palindromes.add(clean_substring)
    return palindromes