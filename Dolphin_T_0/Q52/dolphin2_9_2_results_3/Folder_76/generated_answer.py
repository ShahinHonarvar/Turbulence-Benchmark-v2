def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 257, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes