def if_contains_anagrams(input_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    n = len(input_list)
    for i in range(n):
        for j in range(i + 1, n):
            if len(input_list[i]) >= 3 and len(input_list[j]) >= 3:
                if is_anagram(input_list[i], input_list[j]):
                    anagram_pairs += 1
    return anagram_pairs >= 153