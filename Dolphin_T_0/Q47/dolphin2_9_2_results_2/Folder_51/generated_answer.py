def palindromes_of_specific_lengths(s):
    s = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1].lower() and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes