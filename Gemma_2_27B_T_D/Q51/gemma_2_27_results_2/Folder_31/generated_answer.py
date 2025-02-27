from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = {}
    count = 0
    for word in words:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_counts:
                anagram_counts[sorted_word] += 1
            else:
                anagram_counts[sorted_word] = 1
    for count in anagram_counts.values():
        count = count * (count - 1) // 2
        if count > 65:
            return False
    return True