def palindrome_of_length_n(string):
    string = string.lower()
    set_of_palindromes = set()
    for i in range(len(string) - 84):
        substring = string[i:i + 85]
        if is_palindrome(substring) and is_alpha(substring):
            set_of_palindromes.add(substring)
    return set_of_palindromes

def is_palindrome(string):
    return string == string[::-1]

def is_alpha(string):
    return all(map(str.isalpha, string))