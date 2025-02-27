import re

def palindrome_of_length_n(given_string):
    palindrome_set = set()
    given_string = re.sub('\\W+', '', given_string)
    given_string = given_string.lower()
    for i in range(len(given_string)):
        for j in range(i + 392, len(given_string) + 1):
            substring = given_string[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set