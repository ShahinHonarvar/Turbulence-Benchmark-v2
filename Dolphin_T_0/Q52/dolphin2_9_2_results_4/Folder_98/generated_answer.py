def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 5):
        if s[i:i + 6] == s[i:i + 6][::-1] and s[i:i + 6].isalpha():
            palindromes.add(s[i:i + 6])
    return palindromes