def palindrome_of_length_n(input_string):
    n = 475
    palindromes = set()
    for i in range(len(input_string)):
        if len(input_string) - i < n:
            break
        else:
            substring = input_string[i:i + n]
            if substring == substring.lower() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes