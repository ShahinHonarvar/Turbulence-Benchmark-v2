import re

def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 15, len(input_string)):
            substring = input_string[i:j + 1]
            cleaned_substring = re.sub('[^a-zA-Z]', '', substring).lower()
            if cleaned_substring == cleaned_substring[::-1]:
                palindromes.add(substring)
    return palindromes