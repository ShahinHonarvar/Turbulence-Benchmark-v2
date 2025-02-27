def palindromes_of_specific_lengths(s):
    s = s[3:301]
    s = ''.join((ch for ch in s if ch.isalpha()))
    s = s.lower()
    palindromes = set()
    for length in range(30, 301):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes