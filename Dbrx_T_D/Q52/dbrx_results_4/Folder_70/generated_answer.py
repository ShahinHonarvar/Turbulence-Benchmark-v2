def is_palindrome(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    return string == string[::-1]

def palindrome_of_length_n(input_string, n=401):
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        candidate = input_string[i:i + n]
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes