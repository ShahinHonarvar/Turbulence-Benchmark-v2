def palindromes_of_specific_lengths(s):
    s = s[200:301].lower()
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes