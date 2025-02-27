def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[18:88].lower()
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes