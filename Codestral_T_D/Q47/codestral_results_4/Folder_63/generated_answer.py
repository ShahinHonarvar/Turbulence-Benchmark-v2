def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[33:86]
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes