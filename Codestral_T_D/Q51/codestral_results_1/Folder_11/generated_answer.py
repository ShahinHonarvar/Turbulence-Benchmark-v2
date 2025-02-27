def if_contains_anagrams(lst):
    counter = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in counter:
                counter[sorted_word] = 1
            else:
                counter[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return anagram_pairs <= 41