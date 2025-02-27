def palindrome_of_length_n(input_string):
    palindromes = set()
    for i in range(len(input_string) - 91):
        substring = input_string[i:i + 92].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes