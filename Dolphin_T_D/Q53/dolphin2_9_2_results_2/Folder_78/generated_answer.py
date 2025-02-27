import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    palindromes = set()
    n = 96
    for i in range(len(string) - n + 1):
        sub_string = string[i:i + n]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes