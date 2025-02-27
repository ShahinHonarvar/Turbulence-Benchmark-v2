def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 53):
        substring = string[i:i + 54]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes