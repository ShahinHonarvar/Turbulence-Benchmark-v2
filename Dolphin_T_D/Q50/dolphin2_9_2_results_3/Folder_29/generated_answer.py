def if_contains_anagrams(lst):
    words = dict()
    for word in lst:
        if word not in words and len(word) >= 3:
            words[word] = word.lower()
    anagrams = 0
    for word in words:
        for other_word in words:
            if other_word != word and sorted(words[word]) == sorted(words[other_word]):
                anagrams += 1
                break
    return anagrams >= 35