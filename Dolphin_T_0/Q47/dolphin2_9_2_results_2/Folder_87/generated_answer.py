def palindromes_of_specific_lengths(s):
    s = s[10:94].lower()
    lengths = range(34, 55)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes