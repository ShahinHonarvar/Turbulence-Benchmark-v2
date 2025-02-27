import en_core_web_sm

def if_contains_anagrams(strings_list):
    anagrams = [set([word.lower() for word in set(nlp(string).vocab) if word.lower().isalpha() and len(word) > 2]) for string in strings_list]
    anagram_pairs = sum([sum([1 for j in [x for x in anagrams if x & anagram] for anagram in anagrams if anagram != j]) for anagram in anagrams])
    return anagram_pairs >= 15