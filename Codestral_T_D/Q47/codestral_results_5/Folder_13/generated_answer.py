def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(57, 61):
        for i in range(13, 95 - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes