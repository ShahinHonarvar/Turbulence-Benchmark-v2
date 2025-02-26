def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 209):
        substring = s[i:i + 210]
        if len(substring) == 210 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes