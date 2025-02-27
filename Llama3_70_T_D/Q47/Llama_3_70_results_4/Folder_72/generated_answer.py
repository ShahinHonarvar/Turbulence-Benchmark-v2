def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[26:91]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 27, min(i + 59, len(substr) + 1)):
            substring = substr[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes