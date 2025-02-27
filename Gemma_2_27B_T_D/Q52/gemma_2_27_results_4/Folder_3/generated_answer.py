def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes