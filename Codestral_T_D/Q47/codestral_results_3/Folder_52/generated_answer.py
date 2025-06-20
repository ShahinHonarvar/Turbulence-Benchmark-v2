def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[44:100]
    for length in range(13, 43):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes