def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[30:96]
    for length in range(34, 56):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes