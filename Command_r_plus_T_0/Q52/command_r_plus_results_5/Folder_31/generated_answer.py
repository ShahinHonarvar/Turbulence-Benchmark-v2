def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 65):
        substring = s[i:i + 66]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes