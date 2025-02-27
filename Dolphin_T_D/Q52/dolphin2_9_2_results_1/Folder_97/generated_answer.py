def palindrome_of_length_n(input_string):
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 210, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring.lower() and substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes