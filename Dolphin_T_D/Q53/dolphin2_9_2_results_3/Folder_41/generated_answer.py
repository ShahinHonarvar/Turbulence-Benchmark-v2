import re

def palindrome_of_length_at_least_n(str_input):
    palindromes = set()
    str_input = re.sub('[^a-zA-Z]', '', str_input)
    str_input = str_input.lower()
    for i in range(len(str_input) - 27):
        for length in range(28, len(str_input) - i + 1):
            if len(set(str_input[i:i + length])) != len(str_input[i:i + length]) or str_input[i:i + length] != str_input[i:i + length][::-1]:
                break
            palindromes.add(str_input[i:i + length])
    return palindromes