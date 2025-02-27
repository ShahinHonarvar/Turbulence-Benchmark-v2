def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 86):
        substring = input_string[i:i + 87]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes