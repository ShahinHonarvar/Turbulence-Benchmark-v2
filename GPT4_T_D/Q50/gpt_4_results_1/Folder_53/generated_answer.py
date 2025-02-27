from collections import Counter

def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_counts = Counter(sorted_words)
    pairs_count = sum([count // 2 for count in word_counts.values() if count > 1])
    return pairs_count >= 11