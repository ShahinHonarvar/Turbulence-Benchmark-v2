from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            lowercase_word = word.lower()
            sorted_word = ''.join(sorted(lowercase_word))
            if sorted_word in anagram_counts:
                anagram_counts[sorted_word] += 1
            else:
                anagram_counts[sorted_word] = 1
    return sum((count for count in anagram_counts.values() if count >= 2)) <= 26