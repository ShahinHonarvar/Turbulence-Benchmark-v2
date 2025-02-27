def palindrome_of_length_n(s):
    s = s.lower()
    if len(s) < 42:
        return set()
    palindromes = set()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes