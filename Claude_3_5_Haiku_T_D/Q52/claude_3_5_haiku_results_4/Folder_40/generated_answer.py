def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 2):
        substring = string[i:i + 3]
        if substring[0] == substring[2] and substring.isalpha():
            palindromes.add(substring)
    return palindromes