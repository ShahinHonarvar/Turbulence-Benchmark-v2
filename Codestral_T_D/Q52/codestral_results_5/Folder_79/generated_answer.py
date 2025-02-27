def palindrome_of_length_n(s):
    palindromes = set()
    length = 64
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.lower() == substring[::-1].lower() and substring.isalpha():
            palindromes.add(substring)
    return palindromes