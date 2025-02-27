def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes