def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 136, min(len(s) + 1, i + 161)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes