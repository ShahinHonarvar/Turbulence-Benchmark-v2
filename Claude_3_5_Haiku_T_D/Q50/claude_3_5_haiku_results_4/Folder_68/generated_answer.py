def if_contains_anagrams(input_list):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                anagram_count += 1
                if anagram_count >= 9:
                    return True
    return False