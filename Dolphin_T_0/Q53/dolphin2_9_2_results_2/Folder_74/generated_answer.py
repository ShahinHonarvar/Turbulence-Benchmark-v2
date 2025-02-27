import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('\\\\W+', '', string.lower())
    n = 57
    palindrome_set = set()
    for i in range(len(string) - n + 1):
        for j in range(i + n, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                palindrome_set.add(sub_string)
    return palindrome_set