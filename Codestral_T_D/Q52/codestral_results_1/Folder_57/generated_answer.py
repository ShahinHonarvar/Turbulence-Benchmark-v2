def palindrome_of_length_n(s):
    n = 92
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes