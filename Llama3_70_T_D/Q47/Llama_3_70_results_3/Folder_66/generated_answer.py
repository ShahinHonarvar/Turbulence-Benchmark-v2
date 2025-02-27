def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes