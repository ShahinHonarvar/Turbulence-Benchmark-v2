def palindromes_of_specific_lengths(s):
    s = s[30:96].lower()
    palindromes = set()
    for length in range(34, 56):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes