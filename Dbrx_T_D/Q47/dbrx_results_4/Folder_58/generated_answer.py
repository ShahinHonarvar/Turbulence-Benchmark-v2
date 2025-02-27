def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(109, 127):
        for i in range(125, 284 - length):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes