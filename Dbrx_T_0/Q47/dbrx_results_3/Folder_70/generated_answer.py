def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(24, 53):
        for i in range(10, 71 - length):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes