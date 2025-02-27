def palindromes_of_specific_lengths(s):
    substring = s[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes