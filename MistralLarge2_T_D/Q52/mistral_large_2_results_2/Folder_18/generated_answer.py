def palindrome_of_length_n(string):
    n = 392
    palindromes = set()
    string_lower = string.lower()
    length = len(string_lower)
    for i in range(length - n + 1):
        substring = string_lower[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes