def palindromes_of_specific_lengths(s):
    s = s[29:99]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, min(len(s), i + 10)):
            if s[i:j].lower() == s[i:j].lower()[::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes