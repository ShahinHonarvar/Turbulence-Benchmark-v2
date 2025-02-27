def palindrome_of_length_n(s):
    s = s.lower()
    n = 40
    palindromes = set()
    for i in range(0, len(s)):
        if len(s[i:i + n]) == n:
            if s[i:i + n] == s[i:i + n][::-1]:
                if s[i:i + n].isalpha():
                    palindromes.add(s[i:i + n])
    return palindromes