def palindrome_of_length_n(s):
    palindromes = set()
    length = 99
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes