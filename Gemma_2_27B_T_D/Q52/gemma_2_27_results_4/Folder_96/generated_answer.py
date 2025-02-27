def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 82):
        substring = s[i:i + 83].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes