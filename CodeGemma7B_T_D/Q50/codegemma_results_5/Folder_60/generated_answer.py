from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = []
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append((sorted_word, word))
    combinations_of_pairs = combinations(anagrams, 2)
    count = 0
    for pair in combinations_of_pairs:
        if pair[0][0] == pair[1][0]:
            count += 1
    return count >= 60