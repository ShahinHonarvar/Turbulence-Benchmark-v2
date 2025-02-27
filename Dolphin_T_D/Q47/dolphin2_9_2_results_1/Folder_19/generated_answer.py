def palindromes_of_specific_lengths(s):
    substring = s[9:56]
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes