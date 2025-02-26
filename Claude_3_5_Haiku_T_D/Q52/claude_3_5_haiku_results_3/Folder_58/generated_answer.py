def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 222):
        for j in range(i + 223, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 223 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes