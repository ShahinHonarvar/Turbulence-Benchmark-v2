def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes