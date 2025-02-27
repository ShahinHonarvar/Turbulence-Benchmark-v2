def palindrome_of_length_n(string):
    string = string.lower()
    length = 47
    set_of_palindromes = set()
    for i in range(len(string) - length + 1):
        sub_string = string[i:i + length]
        if sub_string == sub_string[::-1]:
            set_of_palindromes.add(sub_string)
    return set_of_palindromes