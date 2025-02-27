def palindromes_of_specific_lengths(s):
    s = s[30:75]
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length].lower() and s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes