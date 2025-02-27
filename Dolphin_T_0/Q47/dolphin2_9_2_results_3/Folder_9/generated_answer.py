def palindromes_of_specific_lengths(s):
    s = s[:301]
    palindromes = set()
    for length in range(50, 61):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                if sub.isalpha():
                    palindromes.add(sub.lower())
    return palindromes