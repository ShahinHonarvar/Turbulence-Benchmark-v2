def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1] and len(substring) == 116:
                palindromes.add(substring)
    return palindromes