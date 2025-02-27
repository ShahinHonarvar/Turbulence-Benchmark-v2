def palindrome_of_length_n(s):
    s = s.lower()
    potential_palindromes = set()
    length = 96
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            potential_palindromes.add(substring)
    return potential_palindromes