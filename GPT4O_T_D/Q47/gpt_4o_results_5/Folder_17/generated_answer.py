def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(52, 56):
            end = i + j
            if end > len(s):
                break
            substr = s[i:end]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes