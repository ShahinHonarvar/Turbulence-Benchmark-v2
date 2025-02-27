import re

def palindrome_of_length_at_least_n(text):
    input_text = re.sub('[^a-zA-Z]', '', text)
    input_text = input_text.lower()
    input_text_length = len(input_text)
    palindrome_set = set()
    if input_text_length < 13:
        return palindrome_set
    for i in range(input_text_length):
        for j in range(i + 3, input_text_length + 1):
            substring = input_text[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set