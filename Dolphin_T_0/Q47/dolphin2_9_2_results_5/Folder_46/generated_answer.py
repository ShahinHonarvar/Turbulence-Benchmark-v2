def palindromes_of_specific_lengths(s):
    sub = s[11:97]
    lengths = range(29, 63)
    palindromes = set()
    for length in lengths:
        for i in range(len(sub) - length + 1):
            section = sub[i:i + length]
            if section == section.lower() and section == section[::-1]:
                palindromes.add(section)
    return palindromes