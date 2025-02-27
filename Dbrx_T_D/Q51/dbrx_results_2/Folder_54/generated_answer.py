import string

def if_contains_anagrams(str_list):
    anagrams = []
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((c in string.ascii_letters for c in sorted_word)):
            anagrams.append(sorted_word)
    anagram_pairs = len([1 for i, j in zip(anagrams, anagrams[1:]) if i == j])
    return anagram_pairs <= 39