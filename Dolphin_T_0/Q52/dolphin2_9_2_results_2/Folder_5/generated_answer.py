def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 16):
        sub_string = input_string[i:i + 17]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes