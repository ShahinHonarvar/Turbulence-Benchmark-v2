def if_contains_anagrams(input_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagram_pairs(lst):
        anagram_pairs = 0
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                    anagram_pairs += 1
        return anagram_pairs
    return count_anagram_pairs(input_list) <= 11