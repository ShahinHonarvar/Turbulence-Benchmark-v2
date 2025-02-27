def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                if j - i >= 25 and s[i:j].isalpha():
                    palindromes.add(s[i:j])
    return palindromes