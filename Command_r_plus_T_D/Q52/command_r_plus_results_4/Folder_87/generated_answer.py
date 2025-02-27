def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 56):
        substring = s[i:i + 57]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes