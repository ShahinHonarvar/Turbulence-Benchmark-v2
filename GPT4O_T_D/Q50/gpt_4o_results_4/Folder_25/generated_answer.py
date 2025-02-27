from collections import defaultdict

def if_contains_anagrams(words):

    def is_valid_anagram(word1, word2):
        return sorted(word1) == sorted(word2) and len(word1) >= 3 and (len(word2) >= 3)
    word_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        word_groups[sorted_word].append(word.lower())
    anagram_count = 0
    for word_list in word_groups.values():
        if len(word_list) >= 2:
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if is_valid_anagram(word_list[i], word_list[j]):
                        anagram_count += 1
                        if anagram_count >= 14:
                            return True
    return False