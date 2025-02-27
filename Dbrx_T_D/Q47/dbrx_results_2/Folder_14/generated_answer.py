def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 75):
        for length in range(6, 9):
            if i + length <= 75 and s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes