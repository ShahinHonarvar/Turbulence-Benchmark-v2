def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_length(s):
        return len(s) >= 3
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_valid_length(string_list[i]) and is_valid_length(string_list[j]) and is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
    return anagram_pairs <= 68