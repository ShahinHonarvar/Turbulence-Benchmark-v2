from collections import Counter

def if_contains_anagrams(words):
    anagram_dict = {}
    count = 0
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                count += anagram_dict[sorted_word]
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
            if count > 49:
                return False
    return True