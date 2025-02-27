def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(max(0, i - 2), i + 1):
            if s[i:j + i + 1].lower() == s[i:j + i + 1][::-1].lower():
                if len(s[i:j + i + 1]) >= 70:
                    palindromes.add(s[i:j + i + 1].lower())
    return palindromes