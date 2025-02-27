import collections

def if_contains_anagrams(words):

    def count_anagrams(word):
        return ''.join(sorted(word.lower()))
    word_counts = collections.defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram = count_anagrams(word)
            word_counts[anagram] += 1
            if word_counts[anagram] > 70:
                return True
    return False