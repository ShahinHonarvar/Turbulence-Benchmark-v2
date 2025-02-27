def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    palindromes = set()
    for i in range(len(s) - 52):
        for length in range(52, 57):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes