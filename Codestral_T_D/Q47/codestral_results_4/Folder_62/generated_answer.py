def palindromes_of_specific_lengths(s):
    s = s[26:88]
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes