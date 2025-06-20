def palindrome_of_length_n(s):
    s = s.lower()
    n = 17
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring in palindromes:
            continue
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes