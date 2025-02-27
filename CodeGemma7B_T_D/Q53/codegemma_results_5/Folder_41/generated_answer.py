import re

def palindrome_of_length_at_least_n(string):

    def is_palindrome(substring):
        return substring == substring[::-1]
    result = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j].lower()
            if is_palindrome(substring):
                result.add(substring)
    return result