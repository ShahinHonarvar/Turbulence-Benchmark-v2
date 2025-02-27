import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    length = 147
    palindromes = set()
    for i in range(len(string) - length + 1):
        for j in range(i + length, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes