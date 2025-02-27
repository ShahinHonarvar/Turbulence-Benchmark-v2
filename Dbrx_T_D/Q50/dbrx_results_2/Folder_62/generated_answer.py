import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for word in string_list:
        if len(word) >= 3:
            sorted_word = tuple(sorted(word.lower()))
            anagrams.append(sorted_word)
    anagram_counts = [len(list(group)) for value, group in itertools.groupby(sorted(anagrams))]
    return sum(anagram_counts) >= 43