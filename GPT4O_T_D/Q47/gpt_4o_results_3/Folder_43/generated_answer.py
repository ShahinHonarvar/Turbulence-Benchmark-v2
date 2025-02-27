import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        substr = substr.lower()
        return substr == substr[::-1]
    filtered_str = re.sub('[^a-zA-Z]', '', s[41:90])
    result = set()
    for start in range(len(filtered_str)):
        for end in range(start + 23, min(start + 39, len(filtered_str) + 1)):
            substr = filtered_str[start:end]
            if is_palindrome(substr):
                result.add(substr)
    return result