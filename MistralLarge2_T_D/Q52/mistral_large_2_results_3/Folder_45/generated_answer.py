def palindrome_of_length_n(string):
    n = 21
    palindromes = set()
    length = len(string)
    for i in range(length - n + 1):
        substring = string[i:i + n]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes