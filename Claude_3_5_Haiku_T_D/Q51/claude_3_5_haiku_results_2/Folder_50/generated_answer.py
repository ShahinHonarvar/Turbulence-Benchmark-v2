def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagram_pairs(lst):
        anagram_count = 0
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n):
                if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                    anagram_count += 1
        return anagram_count
    return count_anagram_pairs(string_list) <= 47