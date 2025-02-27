def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 28):
        if s[i:i + 29] == s[i:i + 29][::-1]:
            if s[i:i + 29].isalpha():
                palindromes.add(s[i:i + 29])
    return palindromes