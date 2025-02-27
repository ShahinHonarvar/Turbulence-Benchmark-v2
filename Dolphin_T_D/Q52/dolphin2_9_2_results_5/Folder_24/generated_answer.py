def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 29, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1] and set(substring) <= set('abcdefghijklmnopqrstuvwxyz'):
                palindromes.add(substring)
    return palindromes