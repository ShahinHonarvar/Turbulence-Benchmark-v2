def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    seen = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i], lst[j]) and (lst[i], lst[j]) not in seen and ((lst[j], lst[i]) not in seen):
                    anagram_pairs += 1
                    seen.add((lst[i], lst[j]))
                    seen.add((lst[j], lst[i]))
    return anagram_pairs <= 10