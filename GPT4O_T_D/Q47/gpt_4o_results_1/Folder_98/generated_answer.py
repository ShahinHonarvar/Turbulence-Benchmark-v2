import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[:21].lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 5, min(len(s), start + 81)):
            substring = s[start:end + 1]
            cleaned_substring = re.sub('[^a-z]', '', substring)
            if 5 <= len(cleaned_substring) <= 80 and is_palindrome(cleaned_substring):
                palindromes.add(substring)
    return palindromes