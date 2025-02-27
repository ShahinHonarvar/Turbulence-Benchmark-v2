import string

def if_contains_anagrams(words):
    anagrams_count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
                if anagram_dict[sorted_word] == 2:
                    anagrams_count += 1
            else:
                anagram_dict[sorted_word] = 1
    return anagrams_count >= 7