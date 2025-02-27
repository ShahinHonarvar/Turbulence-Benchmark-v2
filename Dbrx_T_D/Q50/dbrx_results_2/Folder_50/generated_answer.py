import string

def if_contains_anagrams(string_list):
    anagrams = []
    for word in string_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower().translate(str.maketrans('', '', string.punctuation))))
        if sorted_word in anagrams:
            anagrams[anagrams.index(sorted_word)] += [''.join(sorted(word.lower().translate(str.maketrans('', '', string.punctuation))))]
        else:
            anagrams.append(''.join(sorted(word.lower().translate(str.maketrans('', '', string.punctuation)))))
    anagram_pairs = [x for x in anagrams if len(x) >= 2]
    return len(anagram_pairs) >= 20