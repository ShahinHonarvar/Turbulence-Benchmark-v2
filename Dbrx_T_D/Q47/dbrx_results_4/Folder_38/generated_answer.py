def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(38, 61):
        for i in range(18, 88 - length + 1):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes