def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(6, 10):
        for i in range(29 - length, 99 - length):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                palindromes.add(s[i:i + length])
    return palindromes