from collections import defaultdict

def if_contains_anagrams(lst_str):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) > 2
    count = defaultdict(int)
    for s in lst_str:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if is_anagram(s[i], s[j]):
                    count[s[i], s[j]] += 1
                    count[s[j], s[i]] += 1
    return sum((val for val in count.values())) <= 39