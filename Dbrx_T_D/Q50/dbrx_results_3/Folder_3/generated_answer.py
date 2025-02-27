import itertools

def if_contains_anagrams(words_list):
    anagrams_dict = {}
    for word in words_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                anagrams_dict[sorted_word] = [word]
    anagram_pairs = [pair for pair in itertools.combinations(anagrams_dict.values(), 2) if len(set(pair[0]) & set(pair[1])) >= 3]
    return len(anagram_pairs) >= 30