def palindromes_of_specific_lengths(s):
    s = s[11:56]
    palindromes = set()
    for length in range(20, 23):
        for index in range(len(s) - length + 1):
            if all((c.isalpha() for c in s[index:index + length])):
                p = s[index:index + length].lower()
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes