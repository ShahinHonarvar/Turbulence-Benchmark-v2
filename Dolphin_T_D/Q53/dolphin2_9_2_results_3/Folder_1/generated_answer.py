def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_palindromes = set()
    for length in range(29, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                set_palindromes.add(substring)
    return set_palindromes