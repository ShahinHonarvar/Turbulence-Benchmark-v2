from collections import defaultdict

def if_contains_anagrams(word_list):

    def sorted_lower(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(int)
    count = 0
    for word in word_list:
        if len(word) >= 3:
            sorted_word = sorted_lower(word)
            count += anagram_groups[sorted_word]
            anagram_groups[sorted_word] += 1
            if count >= 70:
                return True
    return False