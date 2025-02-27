from collections import defaultdict

def if_contains_anagrams(words):

    def count_anagrams(word_list):
        anagram_dict = defaultdict(int)
        count = 0
        for word in word_list:
            if len(word) >= 3:
                sorted_word = ''.join(sorted(word.lower()))
                anagram_dict[sorted_word] += 1
        for value in anagram_dict.values():
            if value > 1:
                count += value * (value - 1) // 2
        return count
    return count_anagrams(words) >= 143