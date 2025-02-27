from collections import defaultdict

def if_contains_anagrams(strs):

    def is_anagram(s, t):
        return sorted(s.lower()) == sorted(t.lower())
    anagram_count = defaultdict(int)
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3 and is_anagram(strs[i], strs[j]):
                anagram_count[strs[i]] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 91