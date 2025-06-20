def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 65):
        substring = s[i:i + 66]
        if len(substring) == 66 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes