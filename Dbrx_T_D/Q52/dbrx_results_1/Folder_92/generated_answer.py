def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

def palindrome_of_length_n(input_string, n):
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes