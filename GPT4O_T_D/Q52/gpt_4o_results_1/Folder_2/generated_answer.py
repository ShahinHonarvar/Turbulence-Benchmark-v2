def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    n = 147
    palindromes = set()
    formatted_string = ''.join(filter(str.isalpha, s.lower()))
    for i in range(len(formatted_string) - n + 1):
        substring = formatted_string[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes