from collections import Counter

def if_contains_anagrams(lst):
    count_letter_pairs = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            pair = (''.join(sorted(Counter(sorted_word).keys())), Counter(sorted_word).values())
            count_letter_pairs.add(pair)
    return len(count_letter_pairs) <= 58 if len(count_letter_pairs) % 2 == 0 else len(count_letter_pairs) < 58