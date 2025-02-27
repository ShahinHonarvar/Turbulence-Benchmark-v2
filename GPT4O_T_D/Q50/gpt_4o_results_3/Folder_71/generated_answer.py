from collections import defaultdict

def if_contains_anagrams(words):

    def sort_word(word):
        return ''.join(sorted(word))
    anagrams = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_word(word.lower())
            count += anagrams[sorted_word]
            anagrams[sorted_word] += 1
    return count >= 57