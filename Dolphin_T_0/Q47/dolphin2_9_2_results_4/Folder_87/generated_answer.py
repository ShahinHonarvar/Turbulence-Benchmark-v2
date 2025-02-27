def palindromes_of_specific_lengths(s):
    s = s[10:93]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length].lower():
                if all((c.isalpha() for c in s[i:i + length])):
                    palindromes.add(s[i:i + length])
    return palindromes