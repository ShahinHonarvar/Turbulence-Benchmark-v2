def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(s[i:j + 1]) < 14:
                continue
            if s[i:j + 1].lower() == s[i:j + 1].lower()[::-1] and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes