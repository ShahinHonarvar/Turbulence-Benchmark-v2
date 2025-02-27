import collections

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def count_anagrams(word_list):
    anagram_count = collections.defaultdict(int)
    for word in word_list:
        sorted_word = tuple(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    return sum((count > 1 for count in anagram_count.values()))

def if_contains_anagrams(word_list):
    return count_anagrams(word_list) <= 26