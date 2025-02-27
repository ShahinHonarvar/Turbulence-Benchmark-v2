def palindrome_of_length_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length - 44):
        substring = s[i:i + 45]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes