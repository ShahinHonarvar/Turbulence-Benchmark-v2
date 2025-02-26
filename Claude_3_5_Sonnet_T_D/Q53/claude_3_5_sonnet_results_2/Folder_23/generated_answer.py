def palindrome_of_length_at_least_n(input_string):
    input_string = ''.join((char.lower() for char in input_string if char.isalpha()))
    n = 19
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        for j in range(i + n, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes