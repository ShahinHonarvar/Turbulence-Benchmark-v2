def palindromes_of_specific_lengths(s):
    s = s[22:78]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if all((c.isalpha() or not c.isalpha() for c in sub.lower())):
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes