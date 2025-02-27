def palindromes_of_specific_lengths(s):
    s = s[31:92]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes