import string

def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((c in string.ascii_lowercase for c in sorted_word)):
            anagrams.append(sorted_word)
    anagram_pairs = len(anagrams) - len(set(anagrams))
    return anagram_pairs <= 181