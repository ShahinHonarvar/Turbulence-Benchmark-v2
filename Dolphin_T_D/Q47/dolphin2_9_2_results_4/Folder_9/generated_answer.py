def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    palindromes = set()
    for i in range(50, 61):
        for j in range(0, 301 - i + 1):
            substr = s[j:j + i]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes