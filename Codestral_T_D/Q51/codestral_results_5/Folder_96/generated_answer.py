def if_contains_anagrams(lst):
    counter = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            counter[sorted_word] = counter.get(sorted_word, 0) + 1
    return sum((value > 2 for value in counter.values())) <= 2