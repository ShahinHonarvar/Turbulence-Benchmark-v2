def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 89, len(s) + 1):
            if s[i:j].lower() == s[i:j][::-1].lower():
                palindromes.add(s[i:j])
    return palindromes