from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for word in string_list:
        cleaned_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(cleaned_word) >= 3:
            sorted_word = ''.join(sorted(cleaned_word))
            anagram_dict[sorted_word].append(cleaned_word)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count <= 6