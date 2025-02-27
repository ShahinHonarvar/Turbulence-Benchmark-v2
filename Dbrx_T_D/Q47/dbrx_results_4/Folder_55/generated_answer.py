def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[10:76].lower()
    for length in range(10, 21):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes