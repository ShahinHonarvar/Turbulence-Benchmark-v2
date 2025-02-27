from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        lowered = s.lower()
        if len(lowered) >= 3:
            sorted_s = ''.join(sorted(lowered))
            anagram_dict[sorted_s] += 1
    pair_count = 0
    for count in anagram_dict.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count >= 219:
                return True
    return False