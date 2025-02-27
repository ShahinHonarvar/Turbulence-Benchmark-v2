from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    anagram_dict = {}
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            counter1 = Counter(lst[i].lower())
            counter2 = Counter(lst[j].lower())
            if counter1 == counter2:
                anagram_pairs += 1
                if lst[i] not in anagram_dict:
                    anagram_dict[lst[i]] = set()
                if lst[j] not in anagram_dict:
                    anagram_dict[lst[j]] = set()
                if lst[j] not in anagram_dict[lst[i]]:
                    anagram_dict[lst[i]].add(lst[j])
                    if len(anagram_dict[lst[i]]) > 1:
                        continue
                if lst[i] not in anagram_dict[lst[j]]:
                    anagram_dict[lst[j]].add(lst[i])
                    if len(anagram_dict[lst[j]]) > 1:
                        continue
        if anagram_pairs >= 21:
            return True
    return False