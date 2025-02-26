def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())

    def count_valid_anagram_pairs(string_list):
        valid_anagram_pairs = 0
        for i in range(len(string_list)):
            for j in range(i + 1, len(string_list)):
                if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                    if is_anagram(string_list[i], string_list[j]):
                        valid_anagram_pairs += 1
        return valid_anagram_pairs
    return count_valid_anagram_pairs(strings) <= 401