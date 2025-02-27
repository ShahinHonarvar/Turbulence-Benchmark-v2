def palindromes_of_specific_lengths(s):
    s = s[:7]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, i + 7):
            if j <= len(s) and s[i:j].lower() == s[i:j].lower()[::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes