import string

def if_contains_anagrams(string_list):
    anagrams = set()
    english_letters = set(string.ascii_letters.lower())
    for word in string_list:
        word = word.lower()
        if len(word) < 3:
            continue
        word_set = set(word) - english_letters
        if len(word_set) <= 2:
            string_set = tuple(sorted(word_set))
            if string_set not in anagrams:
                anagrams.add(string_set)
            else:
                anagrams.remove(string_set)
                anagrams.add(tuple(sorted(word)))
    return len(anagrams) <= 279