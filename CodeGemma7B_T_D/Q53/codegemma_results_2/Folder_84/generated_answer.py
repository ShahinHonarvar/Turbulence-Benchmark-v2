from itertools import product

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    text_set = set(text)
    ans = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word == word[::-1]:
                ans.add(word)
    return ans