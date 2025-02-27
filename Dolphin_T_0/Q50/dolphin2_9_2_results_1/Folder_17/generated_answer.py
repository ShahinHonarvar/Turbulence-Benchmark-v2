import itertools

def if_contains_anagrams(word_list):
    anagrams = {}
    for i in range(len(word_list) - 1):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) < 3 or len(word_list[j]) < 3:
                continue
            sorted_word1 = ''.join(sorted(word_list[i].lower()))
            sorted_word2 = ''.join(sorted(word_list[j].lower()))
            if sorted_word1 == sorted_word2:
                if sorted_word1 not in anagrams:
                    anagrams[sorted_word1] = []
                anagrams[sorted_word1].append(i)
                anagrams[sorted_word1].append(j)
    return len(anagrams) >= 97