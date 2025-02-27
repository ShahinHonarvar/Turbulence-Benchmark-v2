from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_chars(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_dict[sorted_chars(word)].append(word)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 50:
            return True
    return False