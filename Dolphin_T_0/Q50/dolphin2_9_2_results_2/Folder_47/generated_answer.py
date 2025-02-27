def if_contains_anagrams(lst):
    ana_count = 0
    for words in combinations(lst, 2):
        sorted_word1 = ''.join(sorted(words[0].lower()))
        sorted_word2 = ''.join(sorted(words[1].lower()))
        if len(words[0]) >= 3 and len(words[1]) >= 3 and (sorted_word1 == sorted_word2):
            ana_count += 1
    return ana_count >= 47