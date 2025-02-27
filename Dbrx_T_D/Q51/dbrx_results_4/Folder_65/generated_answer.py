import string

def if_contains_anagrams(string_list):

    def words_to_lower_case(words):
        return [word.lower() for word in words]

    def words_to_set_of_sorted_words(words):
        return [''.join(sorted(word)) for word in words]

    def anagram_counter(sorted_words):
        anagram_dict = {}
        for word in sorted_words:
            anagram_dict[word] = anagram_dict.get(word, 0) + 1
        return sum((value * (value - 1) // 2 for value in anagram_dict.values()))
    string_list = words_to_lower_case(string_list)
    sorted_words = words_to_set_of_sorted_words(string_list)
    anagram_pairs = anagram_counter(sorted_words)
    return anagram_pairs <= 72