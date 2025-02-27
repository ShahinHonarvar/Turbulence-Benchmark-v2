from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            for t in anagrams[sorted_s]:
                if s.lower() != t.lower():
                    anagrams[sorted_s].append(s)
                    break
            else:
                anagrams[sorted_s].append(s)
    count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()))
    return count <= 279