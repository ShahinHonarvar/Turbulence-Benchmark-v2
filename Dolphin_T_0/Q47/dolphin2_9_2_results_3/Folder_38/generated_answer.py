def palindromes_of_specific_lengths(s):
    sub = s[17:87]
    palindromes = set()
    for i in range(len(sub) - 37):
        part = sub[i:i + 38]
        if set(part.lower()) <= set('abcdefghijklmnopqrstuvwxyz'):
            if part.lower() == part.lower()[::-1]:
                palindromes.add(part)
    return palindromes