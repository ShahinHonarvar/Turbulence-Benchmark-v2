import re

def palindrome_of_length_n(input_string, length=93):
    palindromes = set()
    input_string = re.sub('[^a-zA-Z]', '', input_string).lower()
    for i in range(len(input_string) - length + 1):
        if input_string[i:i + length] == input_string[i:i + length][::-1]:
            palindromes.add(input_string[i:i + length])
    return palindromes