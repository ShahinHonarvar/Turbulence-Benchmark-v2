def palindromes_of_specific_lengths(s):
    s = s[65:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            bit = s[i:i + length].lower()
            if bit == bit[::-1] and bit.isalpha():
                palindromes.add(bit)
    return palindromes