def palindromes_of_specific_lengths(s):
    s = s[14:72]
    palindromes = set()
    for length in range(19, 56):
        s = s.lower()
        for i in range(len(s) - length + 1):
            if all((c.isalpha() for c in s[i:i + length])):
                if s[i:i + length] == s[i:i + length][::-1]:
                    palindromes.add(s[i:i + length])
    return palindromes