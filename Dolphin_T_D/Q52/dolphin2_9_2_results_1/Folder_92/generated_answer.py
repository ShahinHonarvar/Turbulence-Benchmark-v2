def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 9):
        if s[i:i + 10] == s[i:i + 10][::-1] and s[i:i + 10].isalpha():
            palindromes.add(s[i:i + 10])
    return palindromes