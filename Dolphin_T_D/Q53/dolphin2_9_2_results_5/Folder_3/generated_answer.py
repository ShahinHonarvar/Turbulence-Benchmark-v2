import re

def palindrome_of_length_at_least_n(my_string: str) -> set:
    my_string = re.sub('[^a-zA-Z]', '', my_string)
    my_string = my_string.lower()
    palindromes = set()
    length = len(my_string)
    for i in range(length):
        for j in range(i + 58, length):
            possible_palindrome = my_string[i:j + 1]
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)
    return palindromes