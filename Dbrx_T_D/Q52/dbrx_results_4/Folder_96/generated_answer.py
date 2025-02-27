def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 82):
        for j in range(i + 41, i + 42):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j].lower())
    return palindromes