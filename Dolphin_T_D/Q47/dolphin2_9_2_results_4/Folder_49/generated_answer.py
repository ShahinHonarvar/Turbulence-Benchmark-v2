def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 101):
        for j in range(10, 51):
            if s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                palindromes.add(s[i:i + j].lower())
    return palindromes