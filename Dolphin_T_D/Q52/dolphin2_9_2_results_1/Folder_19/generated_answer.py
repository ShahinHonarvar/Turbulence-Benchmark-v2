def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if len(s) - i < 67:
            break
        elif s[i:i + 67] == s[i:i + 67][::-1]:
            palindromes.add(s[i:i + 67])
    return palindromes