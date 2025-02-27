import string

def sort_characters(word):
    return [''.join(sorted(list(x.lower()))) for x in word if len(x) >= 3]

def anagram_pairs(word_list):
    sorted_words = sort_characters(word_list)
    pairs = []
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j]:
                pairs.append((word_list[i], word_list[j]))
    return pairs

def if_contains_anagrams(word_list):
    return len(anagram_pairs(word_list)) >= 4