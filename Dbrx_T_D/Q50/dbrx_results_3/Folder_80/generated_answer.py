import string

def if_contains_anagrams(string_list):
    anagrams = {}
    for word in string_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word)).encode('utf-8')
        if len(word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    anagram_count = 0
    for count in anagrams.values():
        anagram_count += count // 2
    return anagram_count >= 19