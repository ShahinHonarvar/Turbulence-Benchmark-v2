from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[sorted_chars(word)].append(word)
    count = 0
    for words in anagrams.values():
        n = len(words)
        count += n * (n - 1) // 2
        if count > 113:
            return False
    return True