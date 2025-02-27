def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for length in range(72, len(input_string) + 1):
        for i in range(len(input_string) - length + 1):
            substring = input_string[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes