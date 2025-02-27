def palindrome_of_length_n(input_string):
    palindromes = set()
    letter_input_string = input_string.lower()
    for i in range(len(letter_input_string)):
        for j in range(i + 78, len(letter_input_string) + 1):
            sub_string = letter_input_string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes