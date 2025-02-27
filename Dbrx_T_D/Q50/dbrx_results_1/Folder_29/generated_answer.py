import string

def if_contains_anagrams(word_list):
    anagrams_count = 0
    for word in word_list:
        if len(word) >= 3 and word_exists_in_group(word, word_list):
            anagrams_count += 1
    return anagrams_count >= 35

def word_exists_in_group(word, word_list):
    word = word.lower()
    word = ''.join((c for c in word if c not in string.punctuation))
    group = sorted(word)
    for w in word_list:
        w = w.lower()
        w = ''.join((c for c in w if c not in string.punctuation))
        if sorted(w) == group and word != w:
            return True
    return False