def palindrome_of_length_n(string):
    string = string.lower()
    set_palindromes = set()
    for i in range(len(string) - 20):
        substring = string[i:i + 21]
        if substring == substring[::-1]:
            set_palindromes.add(substring)
    return set_palindromes