from collections import defaultdict

def if_contains_anagrams(str_list):
    letter_counts = defaultdict(int)
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            letter_counts[sorted_word] += 1
    pairs = 0
    for count in letter_counts.values():
        pairs += count - 1
    return pairs <= 34