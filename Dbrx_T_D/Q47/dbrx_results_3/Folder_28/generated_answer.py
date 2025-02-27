def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 72):
        for j in range(21, 33):
            substr = s[i:i + j].lower()
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes