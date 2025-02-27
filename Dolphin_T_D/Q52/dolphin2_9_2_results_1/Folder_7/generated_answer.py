def palindrome_of_length_n(input_string):
    n = 416
    input_string = input_string.lower()
    palindromes = {input_string[i:i + n] for i in range(len(input_string) - n + 1) if input_string[i:i + n] == input_string[i:i + n][::-1]}
    return palindromes