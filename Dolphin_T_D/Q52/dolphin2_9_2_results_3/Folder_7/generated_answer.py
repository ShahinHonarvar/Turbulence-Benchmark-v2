def palindrome_of_length_n(input_string):
    input_length = len(input_string)
    palindromes = set()
    for i in range(input_length):
        for j in range(i + 416, input_length + 1):
            sub_string = input_string[i:j]
            lower_sub_string = sub_string.lower()
            if lower_sub_string == lower_sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes