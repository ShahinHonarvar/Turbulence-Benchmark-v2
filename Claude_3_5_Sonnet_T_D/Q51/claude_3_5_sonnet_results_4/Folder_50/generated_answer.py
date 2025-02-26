from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for word in string_list:
        cleaned_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(cleaned_word) >= 3:
            sorted_word = ''.join(sorted(cleaned_word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(cleaned_word)
            else:
                anagram_dict[sorted_word] = [cleaned_word]
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
            if anagram_count > 47:
                return False
    return True