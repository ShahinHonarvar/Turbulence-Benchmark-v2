def palindrome_of_length_n(s):
    palindromes = set()
    n = len(s)
    for i in range(n - 38):
        substring = s[i:i + 39]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes