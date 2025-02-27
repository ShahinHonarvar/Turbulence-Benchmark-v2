from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_string(word)
            count += anagrams[sorted_word]
            anagrams[sorted_word] += 1
    return count >= 39