def palindromes_of_specific_lengths(s):
    substring = s[45:99]
    lengths = set(range(40, 48))
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            extract = substring[i:i + length]
            if all((char.isalpha() or char.isspace() for char in extract)):
                if extract == extract.lower()[::-1]:
                    palindromes.add(extract)
    return palindromes