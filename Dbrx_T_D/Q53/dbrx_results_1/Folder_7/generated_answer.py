def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(122 - len(s[i:i + 122]), 0, -1):
            if s[i:i + j].lower() == s[i:i + j][::-1].lower():
                palindromes.add(s[i:i + j])
    return palindromes