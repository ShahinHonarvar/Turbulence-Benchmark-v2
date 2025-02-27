from string import ascii_lowercase

def palindrome_of_length_at_least_n(text):
    res = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            word = text[i:j]
            if word == word[::-1] and len(word) >= 25 and word.isalpha():
                res.add(word)
    return res