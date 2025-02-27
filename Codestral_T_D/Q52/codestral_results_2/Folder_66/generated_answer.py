def palindrome_of_length_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length - 24):
        substring = s[i:i + 25]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes