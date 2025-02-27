import itertools

def if_contains_anagrams(strings_list):
    anagrams = [sorted(word.lower()) for word in strings_list if len(word) >= 3]
    anagram_pairs = [pair for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagram_pairs) >= 64