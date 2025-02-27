from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_chars(word):
        return ''.join(sorted(word.lower()))

    def is_valid(word):
        return len(word) >= 3
    anagram_dict = defaultdict(int)
    for word in words:
        if is_valid(word):
            key = sorted_chars(word)
            anagram_dict[key] += 1
    count = 0
    for key in anagram_dict:
        n = anagram_dict[key]
        count += n * (n - 1) // 2
    return count >= 140