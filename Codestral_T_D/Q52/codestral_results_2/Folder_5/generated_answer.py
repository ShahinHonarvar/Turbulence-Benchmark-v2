def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 16):
        substring = string[i:i + 17]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes