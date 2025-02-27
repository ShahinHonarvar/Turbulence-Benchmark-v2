from collections import defaultdict

def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_string(word)
            anagrams[sorted_word] += 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count >= 91:
            return True
    return False