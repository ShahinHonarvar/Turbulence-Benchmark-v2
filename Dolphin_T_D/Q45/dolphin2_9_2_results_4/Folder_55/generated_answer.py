import itertools

def palindromes_between_indices(s):
    letters = ''.join([c for c in s if c.isalpha()])
    if len(letters) < 3:
        return set()
    all_words = set([letters])
    for length in range(3, len(letters) + 1):
        new_words = set()
        for word in all_words:
            for i in range(len(word)):
                for j in range(i + 1, len(word)):
                    new_word = word[:i] + word[j] + word[i + 1:j] + word[i] + word[j + 1:]
                    new_words.add(new_word)
        all_words = new_words
    return {word.lower() for word in all_words if word == word[::-1]}