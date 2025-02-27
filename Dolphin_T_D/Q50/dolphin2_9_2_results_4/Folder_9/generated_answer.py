from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())

    def get_anagrams(lst):
        anagrams = {}
        for i in range(len(lst)):
            if lst[i] not in anagrams.values():
                anagrams[i] = [lst[i]]
            for j in range(i + 1, len(lst)):
                if lst[j] not in anagrams.values():
                    if is_anagram(lst[i], lst[j]):
                        anagrams[i].append(lst[j])
                    else:
                        anagrams[j] = [lst[j]]
        return list(anagrams.values())
    anagrams = get_anagrams(lst)
    return len(anagrams) >= 66 and all((len(s) >= 3 for s in lst))