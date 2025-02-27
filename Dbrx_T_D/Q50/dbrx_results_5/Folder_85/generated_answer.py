import string

def if_contains_anagrams(words):
    anagrams, anagrams_count, words_set = (set(), 0, set())
    for word in words:
        word = word.lower()
        word_set = frozenset(word)
        if len(word) < 3:
            continue
        if word_set in words_set:
            if word_set not in anagrams:
                anagrams.add(word_set)
                anagrams_count += 1
                if anagrams_count >= 73:
                    return True
        else:
            words_set.add(word_set)
    return False