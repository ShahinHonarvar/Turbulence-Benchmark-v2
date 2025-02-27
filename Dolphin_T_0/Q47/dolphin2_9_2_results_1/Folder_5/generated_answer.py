def palindromes_of_specific_lengths(s):
    substring = s[63:71]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes