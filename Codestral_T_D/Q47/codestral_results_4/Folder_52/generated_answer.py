def palindromes_of_specific_lengths(s):
    s = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes