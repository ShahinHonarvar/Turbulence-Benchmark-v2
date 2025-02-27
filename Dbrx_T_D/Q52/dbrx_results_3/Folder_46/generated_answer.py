def get_english_letters(string):
    return ''.join((c for c in string if c.isalpha())).lower()

def is_palindrome(string):
    return string == string[::-1]

def palindrome_of_length_n(string, n):
    string = get_english_letters(string)
    if n % 2 == 0:
        raise ValueError('Length of the palindrome should be odd')
    if n > len(string):
        return set()
    palindromes = set()
    for i in range(len(string) - n + 1):
        if is_palindrome(string[i:i + n]):
            palindromes.add(string[i:i + n])
    return palindromes