def palindrome_of_length_n(s):
    set_of_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 187):
        for j in range(i + 188, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes