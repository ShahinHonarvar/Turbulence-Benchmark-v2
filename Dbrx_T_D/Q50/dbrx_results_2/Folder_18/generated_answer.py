import string

def if_contains_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    pairs = sum((c // 2 for c in anagrams.values()))
    return pairs >= 106