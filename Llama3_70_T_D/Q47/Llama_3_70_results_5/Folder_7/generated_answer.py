def palindromes_of_specific_lengths(s):
    substr = s[119:257].lower()
    palindromes = set()
    for i in range(len(substr) - 123 + 1):
        for j in range(i + 104 - 1, min(i + 123, len(substr))):
            sub = substr[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes