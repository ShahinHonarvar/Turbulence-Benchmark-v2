def palindromes_of_specific_lengths(s):
    s = s[10:71]
    palindromes = set()
    for length in range(24, 53):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes