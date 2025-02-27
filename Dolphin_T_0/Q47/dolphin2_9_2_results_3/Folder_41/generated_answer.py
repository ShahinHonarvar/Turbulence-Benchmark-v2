def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindrommes