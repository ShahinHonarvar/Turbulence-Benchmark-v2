def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 5):
        for j in range(i, i + 6):
            if s[i].lower() == s[j].lower():
                palindromes.add(s[i:j + 1])
    return palindromes