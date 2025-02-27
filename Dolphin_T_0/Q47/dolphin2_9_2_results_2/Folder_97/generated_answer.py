def palindromes_of_specific_lengths(s):
    s = s[27:95]
    palindromes = set()
    for length in range(38, 50):
        for i in range(0, len(s) - length + 1):
            subset = s[i:i + length]
            if subset == subset[::-1] and subset.isalpha('english'):
                palindromes.add(subset.lower())
    return palindromes