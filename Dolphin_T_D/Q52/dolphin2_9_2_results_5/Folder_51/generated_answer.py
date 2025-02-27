def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 72):
        substring = input_string[i:i + 73]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes