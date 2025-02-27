def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 80 + 1):
        substring = s[i:i + 80]
        if substring.lower() == substring[::-1].lower() and substring.isalpha():
            palindromes.add(substring)
    return palindromes