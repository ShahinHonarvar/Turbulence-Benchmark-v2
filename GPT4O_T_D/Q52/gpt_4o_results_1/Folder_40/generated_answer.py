def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 2):
        if s[i:i + 3] == s[i:i + 3][::-1]:
            if s[i:i + 3].isalpha():
                palindromes.add(s[i:i + 3])
    return palindromes