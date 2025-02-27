def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 400):
        substring = s[i:i + 401]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes