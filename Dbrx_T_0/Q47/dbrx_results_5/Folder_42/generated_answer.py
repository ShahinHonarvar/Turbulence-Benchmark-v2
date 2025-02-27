def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(18, 48):
        for i in range(43, 96 - length):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes