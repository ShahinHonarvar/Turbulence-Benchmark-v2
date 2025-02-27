def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes