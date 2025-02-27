import re

def palindrome_of_length_at_least_n(user_input):
    user_input = re.sub('[^a-zA-Z]', '', user_input).lower()
    palindrome_set = set()
    for i in range(len(user_input)):
        for j in range(i + 57, len(user_input) + 1):
            substring = user_input[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set