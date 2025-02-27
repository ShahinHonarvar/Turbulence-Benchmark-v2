from collections import defaultdict

def if_contains_anagrams(word_list):
    words = defaultdict(list)
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        words[sorted_word].append(word)
    for anagram_list in words.values():
        if len(anagram_list) >= 3:
            for i in range(len(anagram_list)):
                for j in range(i + 1, len(anagram_list)):
                    if anagram_list[i].lower() == anagram_list[j].lower():
                        return True
    return False