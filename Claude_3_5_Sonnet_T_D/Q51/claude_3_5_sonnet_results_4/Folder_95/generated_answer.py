from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    word_dict = defaultdict(list)
    for word in string_list:
        cleaned_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(cleaned_word) >= 3:
            sorted_word = ''.join(sorted(cleaned_word))
            word_dict[sorted_word].append(cleaned_word)
    for anagram_group in word_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_count <= 6