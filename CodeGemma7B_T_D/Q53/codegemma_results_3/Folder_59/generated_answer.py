from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    palindrome = defaultdict(set)
    text = text.lower()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1] and len(text[i:j + 1]) >= 20:
                palindrome[text[i:j + 1]].add(text[i:j + 1])
    return palindrome.keys()