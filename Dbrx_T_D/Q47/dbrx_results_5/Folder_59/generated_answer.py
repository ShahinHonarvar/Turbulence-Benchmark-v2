def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(3, 16):
        for i in range(101 - length):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes