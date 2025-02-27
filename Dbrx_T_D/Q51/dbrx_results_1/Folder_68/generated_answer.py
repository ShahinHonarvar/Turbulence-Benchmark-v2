import string

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((c in string.ascii_lowercase for c in sorted_word)):
            anagrams.append(sorted_word)
    anagram_counts = {anagram: anagrams.count(anagram) for anagram in set(anagrams)}
    return sum((count // 2 for count in anagram_counts.values())) <= 94