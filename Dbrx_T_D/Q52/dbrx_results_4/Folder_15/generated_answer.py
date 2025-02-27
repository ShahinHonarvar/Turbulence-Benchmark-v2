def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 2, len(s) - 1):
            if s[i] == s[j] and s[i + 1] == s[j - 1]:
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if p.lower() == p}