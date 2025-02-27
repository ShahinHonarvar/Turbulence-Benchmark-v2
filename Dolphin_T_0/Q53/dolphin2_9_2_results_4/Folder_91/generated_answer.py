def palindrome_of_length_at_least_n(s):
    palindromes = set()
    string = s.lower()
    length = len(string)
    for size in range(7, length + 1):
        for start in range(0, length - size + 1):
            substring = string[start:start + size]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes