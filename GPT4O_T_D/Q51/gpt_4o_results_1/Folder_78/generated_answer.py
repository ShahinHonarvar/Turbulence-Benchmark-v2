from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    normalized = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    pairs = 0
    counted_pairs = set()
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if normalized[i] == normalized[j]:
                pair = tuple(sorted((lst[i], lst[j])))
                if pair not in counted_pairs:
                    counted_pairs.add(pair)
                    pairs += 1
                if pairs > 70:
                    return False
    return True