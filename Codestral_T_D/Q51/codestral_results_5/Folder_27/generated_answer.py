from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    counter_list = [Counter(s.lower()) for s in strings if len(s) >= 3]
    for i in range(len(counter_list)):
        for j in range(i + 1, len(counter_list)):
            if counter_list[i] == counter_list[j]:
                anagram_count += 1
    return anagram_count <= 113