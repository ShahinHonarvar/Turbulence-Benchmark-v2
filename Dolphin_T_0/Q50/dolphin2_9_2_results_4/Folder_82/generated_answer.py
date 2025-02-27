def if_contains_anagrams(lst):
    counter = 0
    pairs = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            pairs.add(sorted_word)
    return len(pairs) >= 276