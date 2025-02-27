def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    palindromes = set()
    for i in range(0, 53):
        for j in range(52 - i, 53 - i):
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes