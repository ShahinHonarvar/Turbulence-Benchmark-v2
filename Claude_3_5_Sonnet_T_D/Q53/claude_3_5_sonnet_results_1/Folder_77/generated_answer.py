def palindrome_of_length_at_least_n(input_string):
    input_string = ''.join((char.lower() for char in input_string if char.isalpha()))
    palindromes = set()
    length = len(input_string)
    for i in range(length):
        for j in range(i + 149, length + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes