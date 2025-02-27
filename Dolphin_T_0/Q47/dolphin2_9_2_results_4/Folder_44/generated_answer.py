def palindromes_of_specific_lengths(s):
    s = s[17:99].lower()
    palindromes = set()
    for length in range(31, 52):
        for start in range(len(s) - length + 1):
            if all((c.isalpha() for c in s[start:start + length])):
                if s[start:start + length] == s[start:start + length][::-1]:
                    palindromes.add(s[start:start + length])
    return palindromes