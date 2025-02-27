def palindrome_of_length_n(s):
    all_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if substring == substring[::-1]:
            all_palindromes.add(substring)
    return all_palindromes