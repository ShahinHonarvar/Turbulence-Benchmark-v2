def palindrome_of_length_n(str):
    palindromes = set()
    for i in range(len(str) - 422):
        substring = str[i:i + 423]
        if is_palindrome(substring.lower()):
            palindromes.add(substring)
    return palindromes

def is_palindrome(str):
    return str == str[::-1]