def palindromes_of_specific_lengths(s):
    s = s[30:75]
    palindromes_set = set()
    for length in range(23, 40):
        for i in range(0, len(s) - length + 1):
            string = s[i:i + length]
            string = ''.join([c for c in string if c.isalpha()])
            if string.lower() == string.lower()[::-1]:
                palindromes_set.add(string)
    return palindromes_set