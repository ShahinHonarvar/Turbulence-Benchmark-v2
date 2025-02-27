import re

def palindrome_of_length_n(input_string):
    input_string = re.sub('[^a-zA-Z]', '', input_string)
    input_string = input_string.lower()
    n = 279
    if len(input_string) != n:
        return set()
    palindromeSet = set()
    for i in range(0, len(input_string)):
        for j in range(i + n - 1, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1]:
                palindromeSet.add(sub_string)
    return palindromeSet