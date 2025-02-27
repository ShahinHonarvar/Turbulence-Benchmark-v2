def palindromes_of_specific_lengths(s):
    s = s[25:88]
    palindromes = set()
    for i in range(52, 57):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1]:
                if sub.isalpha():
                    palindromes.add(sub.lower())
    return palindromes