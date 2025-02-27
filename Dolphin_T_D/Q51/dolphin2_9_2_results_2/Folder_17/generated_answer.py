from collections import Counter

def if_contains_anagrams(square_list):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return Counter(s1) == Counter(s2)

    def is_valid_length(s):
        return len(s) >= 3
    res = 0
    for i in range(0, len(square_list)):
        for j in range(i + 1, len(square_list)):
            if is_valid_length(square_list[i]) and is_valid_length(square_list[j]) and is_anagram(square_list[i], square_list[j]):
                res += 1
    return res <= 22