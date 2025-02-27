def palindromes_of_specific_lengths(s):
    substring = s[17:87]
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes