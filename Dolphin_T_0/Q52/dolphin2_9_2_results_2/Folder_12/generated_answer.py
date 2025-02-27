def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        if len(input_string[i:i + 23]) == 23:
            if input_string[i:i + 23] == input_string[i:i + 23][::-1]:
                palindromes.add(input_string[i:i + 23])
    return palindromes