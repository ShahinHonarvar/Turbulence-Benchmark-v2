def palindrome_of_length_n(input_string):
    len_input_string = len(input_string)
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len_input_string - 317):
        sub_string = input_string[i:i + 318]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes