from collections import defaultdict
from string import ascii_lowercase

def palindrome_of_length_n(text):

    def letters_of_word(word):
        return ''.join(sorted(list(filter(str.isalpha, word))))
    letters = defaultdict(list)
    for i in range(len(text)):
        for j in range(i + 94, len(text) + 1):
            word = letters_of_word(text[i:j])
            letters.setdefault(word, []).append(i)
    return {text[i:i + 93] for word in letters.keys() if len(word) == 93 for i in letters[word]}