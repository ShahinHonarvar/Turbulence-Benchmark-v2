from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for words in anagram_dict.values():
        if len(words) > 1 and len(words[0]) >= 3:
            count += len(words) * (len(words) - 1) // 2
    return count >= 18