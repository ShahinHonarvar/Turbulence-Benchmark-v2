def palindrome_of_length_at_least_n(string):
    string = string.lower()
    set_of_palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) >= 21:
                set_of_palindromes.add(substring)
    return set_of_palindromes