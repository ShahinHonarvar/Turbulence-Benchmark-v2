def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes