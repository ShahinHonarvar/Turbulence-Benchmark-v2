import re

def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    input_string = re.sub('[^a-zA-Z]', '', input_string)
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 26, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes