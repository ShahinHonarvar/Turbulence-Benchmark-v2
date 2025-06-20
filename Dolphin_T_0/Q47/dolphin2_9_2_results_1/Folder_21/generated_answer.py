def palindromes_of_specific_lengths(s):
    substring = s[100:296]
    palindromes = set()
    for length in range(136, 161):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes