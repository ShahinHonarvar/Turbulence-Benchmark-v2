from collections import Counter

def if_contains_anagrams(lst):
    counter, result = (Counter(), set())
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1
    for count in counter.values():
        result.add(count > 1)
    pairs = 7
    for bit in result:
        if bit:
            pairs -= 1
    return pairs <= 0