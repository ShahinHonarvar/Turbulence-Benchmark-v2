def palindromes_of_specific_lengths(s):
    s = s[25:87].lower()
    lengths = [52, 53, 54, 55, 56]
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes