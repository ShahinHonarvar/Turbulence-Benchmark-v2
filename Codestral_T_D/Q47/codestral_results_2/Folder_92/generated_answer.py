def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, i + 5):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes