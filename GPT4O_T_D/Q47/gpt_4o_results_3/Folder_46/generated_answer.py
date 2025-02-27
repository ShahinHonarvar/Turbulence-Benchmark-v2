import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    start, end = (11, 97)
    min_len, max_len = (29, 62)
    substring = s[start:end + 1]
    filtered_substring = re.sub('[^a-zA-Z]', '', substring)
    palindromes = set()
    for i in range(len(filtered_substring)):
        for j in range(i + min_len, min(i + max_len + 1, len(filtered_substring) + 1)):
            sub = filtered_substring[i:j]
            if len(sub) >= min_len and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes