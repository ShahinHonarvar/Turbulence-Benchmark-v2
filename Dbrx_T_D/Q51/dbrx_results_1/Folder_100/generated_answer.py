import itertools

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for i in range(len(sorted_word) - 1):
            for j in range(i + 1, len(sorted_word)):
                anagram = ''.join((c for c in sorted_word if c not in sorted_word[i:j + 1]))
                if anagram and anagram != sorted_word and (anagram.lower() in lst):
                    anagram_pairs += 1
                    if anagram_pairs > 98:
                        return False
    return True