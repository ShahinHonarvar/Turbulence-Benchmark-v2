from collections import defaultdict

def if_contains_anagrams(str_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    length_dict = defaultdict(list)
    for s in str_list:
        length_dict[len(s)].append(s)
    for length, strings in length_dict.items():
        if length < 3:
            continue
        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                if is_anagram(strings[i], strings[j]):
                    anagram_count += 1
                    if anagram_count >= 10:
                        return True
    return False