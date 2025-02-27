from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    res = defaultdict(set)
    for i in range(len(text)):
        for j in range(i + 2, len(text) + 1):
            word = text[i:j]
            if word == word[::-1]:
                res[len(word)].add(word)
    return res.get(37, set())