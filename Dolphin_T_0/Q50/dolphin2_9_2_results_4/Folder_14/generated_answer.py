from collections import Counter

def if_contains_anagrams(word_list):
    counter = Counter()
    for word in word_list:
        if len(word) < 3 or not word.isalpha():
            continue
        sorted_word = ''.join(sorted(word.lower()))
        counter[sorted_word] += 1
    count = sum((1 for v in counter.values() if v >= 2))
    return count >= 44