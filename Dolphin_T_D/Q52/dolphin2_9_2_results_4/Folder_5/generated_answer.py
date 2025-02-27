def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 16):
        substring = input_string[i:i + 17]
        if substring == substring[::-1].replace(' ', ''):
            palindromes.add(substring)
    return palindromes