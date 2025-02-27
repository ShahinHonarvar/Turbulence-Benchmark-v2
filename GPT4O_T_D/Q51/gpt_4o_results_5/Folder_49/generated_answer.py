from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word))
    lower_words = [word.lower() for word in words]
    anagram_dict = defaultdict(list)
    for word in lower_words:
        if len(word) >= 3:
            anagram_dict[normalize(word)].append(word)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values()))
    return anagram_pairs <= 10