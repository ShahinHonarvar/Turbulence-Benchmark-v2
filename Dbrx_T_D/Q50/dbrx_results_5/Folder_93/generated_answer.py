import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for word_tuple in itertools.combinations(string_list, 2):
        if len(set(word_tuple[0])) >= 3 and len(set(word_tuple[1])) >= 3 and (sorted(word_tuple[0].lower()) == sorted(word_tuple[1].lower())):
            anagrams_count += 1
    return anagrams_count >= 18