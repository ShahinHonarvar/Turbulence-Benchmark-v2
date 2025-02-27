from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = set()
    word_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_count[sorted_word] += 1
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if word_count[sorted_word] > 1:
                anagram_pairs.update(((word, other) for other in lst if is_anagram(word, other) and word != other))
    return len(anagram_pairs) <= 276