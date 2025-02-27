def palindromes_of_specific_lengths(s):
    s = s[1:300]
    s = s.lower()
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes