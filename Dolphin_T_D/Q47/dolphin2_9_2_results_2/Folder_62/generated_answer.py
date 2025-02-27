def palindromes_of_specific_lengths(s):
    substring = s[26:88]
    lengths = range(52, 57)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes