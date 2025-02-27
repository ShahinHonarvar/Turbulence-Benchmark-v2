def palindromes_of_specific_lengths(s):
    substring = s[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes