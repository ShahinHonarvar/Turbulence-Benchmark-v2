def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes