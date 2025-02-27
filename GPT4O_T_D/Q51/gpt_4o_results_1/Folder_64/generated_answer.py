def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = 0
    lowercased_list = [s.lower() for s in lst]
    for i in range(len(lowercased_list)):
        for j in range(i + 1, len(lowercased_list)):
            if len(lowercased_list[i]) >= 3 and len(lowercased_list[j]) >= 3:
                if is_anagram(lowercased_list[i], lowercased_list[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 59:
                        return False
    return True