import itertools
        import re

def palindrome_of_length_at_least_n(str):
    str = str.lower()
    str = re.sub('[^a-z]', '', str)
    result = set()
    for n in range(49, len(str) + 1):
        for left in range(len(str) - n + 1):
            right = left + n - 1
            palindrome = str[left:right + 1]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result