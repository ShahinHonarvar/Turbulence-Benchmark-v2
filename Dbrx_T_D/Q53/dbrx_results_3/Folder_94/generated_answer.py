def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 41, len(s) + 1):
            if s[i:j].lower() == s[i:j][::-1].lower() and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes