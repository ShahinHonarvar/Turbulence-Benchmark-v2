from collections import defaultdict

def palindrome_of_length_at_least_n(text):

    def is_palindrome(text):
        return text == text[::-1]
    palindrome = defaultdict(set)
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            s = text[i:j].lower()
            if is_palindrome(s) and len(s) >= 133:
                palindrome[len(s)].add(s)
    return palindrome or {}