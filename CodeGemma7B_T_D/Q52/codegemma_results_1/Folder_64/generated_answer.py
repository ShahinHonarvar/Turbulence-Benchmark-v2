def palindrome_of_length_n(string):
    low_str = string.lower()
    palindromes = set()
    palindrome_length = 9
    for start in range(len(low_str) - palindrome_length + 1):
        substring = low_str[start:start + palindrome_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes