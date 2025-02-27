def palindrome_of_length_n(s):
    s = s.lower()
    n = 80
    letters_only = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(letters_only) - n + 1):
        substring = letters_only[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes