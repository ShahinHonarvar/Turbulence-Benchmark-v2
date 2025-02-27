def palindromes_of_specific_lengths(s):
    s = s[63:71]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes