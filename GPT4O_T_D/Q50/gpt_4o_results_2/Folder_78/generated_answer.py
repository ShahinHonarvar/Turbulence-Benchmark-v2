from collections import defaultdict

def if_contains_anagrams(words):

    def normalized(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagrams[normalized(word)] += 1
    count_anagrams = 0
    for count in anagrams.values():
        count_anagrams += count * (count - 1) // 2
        if count_anagrams >= 79:
            return True
    return False