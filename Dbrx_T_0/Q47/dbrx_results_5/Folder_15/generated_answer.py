def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(3, 7):
        for i in range(7 - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes