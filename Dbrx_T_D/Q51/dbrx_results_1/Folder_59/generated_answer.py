import string

def if_contains_anagrams(lst):
    anagrams = set()
    max_anagrams_count = 15
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        anagram_key = ''.join(sorted(set(sorted_word)))
        if len(anagram_key) >= 3 and anagram_key not in anagrams and word.translate(str.maketrans('', '', string.punctuation)).isalpha():
            anagrams.add(anagram_key)
    return len(anagrams) <= max_anagrams_count