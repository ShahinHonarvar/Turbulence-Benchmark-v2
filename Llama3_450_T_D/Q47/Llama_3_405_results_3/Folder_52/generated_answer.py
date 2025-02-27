def palindromes_of_specific_lengths(s):
    substr = s[44:100].lower()
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes