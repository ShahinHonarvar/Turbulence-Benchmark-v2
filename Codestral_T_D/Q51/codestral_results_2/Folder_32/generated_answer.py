def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    anagram_pairs = sum((len(anagrams[word]) * (len(anagrams[word]) - 1) // 2 for word in anagrams))
    return anagram_pairs <= 89