def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def preprocess(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in string_list:
        if len(word) >= 3:
            processed_word = preprocess(word)
            if processed_word in anagram_dict:
                anagram_dict[processed_word] += 1
            else:
                anagram_dict[processed_word] = 1
    count = sum((min(count, 2) for count in anagram_dict.values()))
    return count <= 3