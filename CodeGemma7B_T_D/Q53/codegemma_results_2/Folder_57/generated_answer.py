from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    answer = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(text)):
        for j in range(i, len(text)):
            word = text[i:j + 1]
            if len(word) < 93:
                continue
            if word.isalpha():
                if is_palindrome(word):
                    answer.add(word)
    return answer