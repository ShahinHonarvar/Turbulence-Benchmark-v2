def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 37):
        for j in range(i, i + 38):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower():
                palindromes.add(s[i:j + 1])
    return palindromes