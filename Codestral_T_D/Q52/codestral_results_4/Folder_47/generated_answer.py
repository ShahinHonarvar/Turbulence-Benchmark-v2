def palindrome_of_length_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length - 33):
        substring = s[i:i + 34]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes