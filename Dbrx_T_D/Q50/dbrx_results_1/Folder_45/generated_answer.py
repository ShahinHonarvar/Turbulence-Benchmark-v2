def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams.append(sorted_word)
    unique_anagrams = set(anagrams)
    anagram_pairs = sum((x < y for x in anagrams for y in unique_anagrams if x != y)) // 2
    return anagram_pairs >= 277