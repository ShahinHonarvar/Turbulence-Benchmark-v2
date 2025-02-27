def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 115, len(input_string)):
            substring = input_string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes