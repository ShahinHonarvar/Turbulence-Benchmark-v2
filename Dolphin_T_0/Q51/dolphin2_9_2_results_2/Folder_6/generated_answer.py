from collections import Counter

def if_contains_anagrams(word_list):
    letter_counts = {}
    word_pairs = []
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in letter_counts:
                letter_counts[sorted_word] = 1
            else:
                letter_counts[sorted_word] += 1
            if letter_counts[sorted_word] > 1:
                word_pairs.append(word)
    return len(word_pairs) <= 86