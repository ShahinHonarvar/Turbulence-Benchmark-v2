def if_contains_anagrams(input_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) >= 3 and len(input_list[j]) >= 3:
                if is_anagram(input_list[i], input_list[j]):
                    anagram_pairs += 1
    return anagram_pairs <= 97