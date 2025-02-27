def palindrome_of_length_n(string):
    string = string.lower()
    length = 74
    palindromes_set = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes_set.add(substring)
    return palindromes_set