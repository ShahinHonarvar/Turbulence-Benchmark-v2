def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[16:78]
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes