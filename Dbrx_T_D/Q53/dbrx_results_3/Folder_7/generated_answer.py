def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and len(s[i:j + 1]) >= 122 and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes