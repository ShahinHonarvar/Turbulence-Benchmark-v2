import string

def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagrams:
                anagrams.append(sorted_word)
    num_anagrams = len(anagrams)
    return True if num_anagrams >= 78 else False