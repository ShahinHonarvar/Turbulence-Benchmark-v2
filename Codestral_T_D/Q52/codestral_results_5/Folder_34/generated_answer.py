def palindrome_of_length_n(s):
    length = 33
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(s[i:i + length])
    return palindromes