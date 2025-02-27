def palindrome_of_length_n(s):
    n = 20
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes