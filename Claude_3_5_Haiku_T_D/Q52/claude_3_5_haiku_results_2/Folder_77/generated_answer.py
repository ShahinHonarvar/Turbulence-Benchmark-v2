def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 172):
        substring = s[start:start + 173]
        if len(substring) == 173 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes