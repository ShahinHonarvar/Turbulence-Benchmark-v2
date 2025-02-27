from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(set)
    count = 0
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in d and word not in d[sorted_word]:
                count += len(d[sorted_word])
            d[sorted_word].add(word)
    return count >= 30