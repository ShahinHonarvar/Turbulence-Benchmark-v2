import re

def is_english_and_long_enough(word):
    return re.match('^[a-zA-Z]{3,}$', word)

def remove_duplicates(words):
    return list(set(words))

def get_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if is_english_and_long_enough(sorted_word):
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
    return anagrams

def if_contains_anagrams(words):
    anagrams = get_anagrams(words)
    return sum((len(anagrams[word]) for word in anagrams)) <= 42