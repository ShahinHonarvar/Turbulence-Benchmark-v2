def palindromes_of_specific_lengths(s):
    s = s[70:141]
    palindromes = set()
    for length in range(3, 61):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length].lower())
    return palindromes