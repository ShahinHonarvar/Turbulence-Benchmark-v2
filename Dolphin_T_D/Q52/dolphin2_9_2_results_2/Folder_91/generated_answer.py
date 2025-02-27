def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    length = len(string)
    for i in range(length - 6):
        sub_string = string[i:i + 7]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes