def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 3):
        if s[i:i + 4] == s[i:i + 4][::-1] and s[i:i + 4].isalpha():
            palindromes.add(s[i:i + 4])
    return palindromes