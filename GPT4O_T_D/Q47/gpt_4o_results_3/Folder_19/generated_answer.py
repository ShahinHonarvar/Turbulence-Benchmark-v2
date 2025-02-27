def palindromes_of_specific_lengths(s):
    s = s[10:56].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(3, 8):
            if i + j <= len(s):
                substr = s[i:i + j]
                if substr.isalpha() and substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes