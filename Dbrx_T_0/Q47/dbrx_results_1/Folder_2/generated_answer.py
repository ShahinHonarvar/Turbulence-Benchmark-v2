def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 60):
        for length in range(18, 37):
            if i + length <= 60 and s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length].lower())
    return palindromes