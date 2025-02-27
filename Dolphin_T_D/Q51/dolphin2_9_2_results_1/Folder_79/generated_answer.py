from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    count = 0
    for word in strings:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            counter[sorted_word] += 1
            count = max(count, counter[sorted_word])
    return count <= 173