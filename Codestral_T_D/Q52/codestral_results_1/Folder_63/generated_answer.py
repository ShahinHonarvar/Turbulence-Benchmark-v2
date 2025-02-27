def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 17):
        substring = s[i:i + 18].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(s[i:i + 18])
    return palindromes