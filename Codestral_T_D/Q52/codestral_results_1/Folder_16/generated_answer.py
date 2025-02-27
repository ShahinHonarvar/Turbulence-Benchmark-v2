def palindrome_of_length_n(s):
    length = 255
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes