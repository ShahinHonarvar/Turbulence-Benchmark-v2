import string

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and all((c in string.ascii_letters for c in sorted_word)):
            anagrams.append(sorted_word)
    anagram_counts = {}
    for anagram in anagrams:
        if anagram not in anagram_counts:
            anagram_counts[anagram] = 1
        else:
            anagram_counts[anagram] += 1
    if sum((count <= 25 for count in anagram_counts.values())) == len(anagram_counts):
        return True
    return False