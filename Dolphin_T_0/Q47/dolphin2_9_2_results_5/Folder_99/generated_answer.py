def palindromes_of_specific_lengths(s):
    sub = s[127:289]
    palindromes = set()
    for length in range(119, 142):
        for i in range(0, len(sub) - length + 1):
            section = sub[i:i + length].lower()
            if set(section) <= set('abcdefghijklmnopqrstuvwxyz'):
                if section == section[::-1]:
                    palindromes.add(section)
    return palindromes