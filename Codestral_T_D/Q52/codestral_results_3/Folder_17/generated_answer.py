def palindrome_of_length_n(s):
    length = 289
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes