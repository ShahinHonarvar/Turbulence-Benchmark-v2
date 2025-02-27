import string

def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in words:
        sorted_word = sort_string(word)
        if len(sorted_word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    pairs = 0
    for words in anagrams.values():
        pairs += len(words) * (len(words) - 1) // 2
        if pairs >= 46:
            return True
    return False