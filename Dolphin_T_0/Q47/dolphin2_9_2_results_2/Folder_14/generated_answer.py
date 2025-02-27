def palindromes_of_specific_lengths(s):
    palindromes_set = set()
    for length in range(6, 9):
        for i in range(9, 74):
            substr = s[i:i + length]
            if substr.lower() == substr.lower()[::-1] and substr.isalpha():
                palindromes_set.add(substr)
    return palindromes_set