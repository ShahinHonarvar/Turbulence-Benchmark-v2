def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 80):
        substring = s[i:i + 81]
        if substring == substring[::-1] and all((char.isalpha() for char in substring)):
            palindromes.add(substring)
    return palindromes