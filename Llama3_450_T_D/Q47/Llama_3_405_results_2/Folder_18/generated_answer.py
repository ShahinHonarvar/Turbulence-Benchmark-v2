def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes