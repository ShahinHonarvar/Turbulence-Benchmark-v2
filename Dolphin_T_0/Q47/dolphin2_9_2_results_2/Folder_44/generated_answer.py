def palindromes_of_specific_lengths(s):
    s = s[18:99]
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            sub = ''.join((ch for ch in sub if ch.isalpha()))
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes