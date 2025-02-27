def palindromes_of_specific_lengths(s):
    s = s[35:93].lower()
    lengths = range(10, 36)
    palindromes = set()
    for length in lengths:
        for i in range(0, len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes