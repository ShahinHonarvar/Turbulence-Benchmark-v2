import itertools

def if_contains_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
    anagram_pairs = sum((len(anagrams[k]) // 2 for k in anagrams))
    return anagram_pairs >= 10