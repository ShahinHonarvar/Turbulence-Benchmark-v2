def if_contains_anagrams(list_of_strings):

    def sort_word(word):
        return ''.join(sorted(word.lower()))

    def count_pairs(anagram_dict):
        return len(anagram_dict.values())
    anagram_dict = {}
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = sort_word(word)
            anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    return count_pairs(anagram_dict) <= 25