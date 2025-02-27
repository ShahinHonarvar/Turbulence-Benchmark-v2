import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 4, len(string) + 1):
            string_slice = string[i:j]
            if string_slice == string_slice[::-1]:
                palindromes.add(string_slice)
    return palindromes