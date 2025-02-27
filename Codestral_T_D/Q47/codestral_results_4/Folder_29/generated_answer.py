def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[15:95]
    for length in range(18, 74):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes