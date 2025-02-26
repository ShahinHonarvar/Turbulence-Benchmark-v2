def if_contains_anagrams(input_list):

    def is_anagram(str1, str2):
        return len(str1) == len(str2) and len(str1) >= 3 and (sorted(str1.lower()) == sorted(str2.lower()))
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 64:
                    return False
    return True