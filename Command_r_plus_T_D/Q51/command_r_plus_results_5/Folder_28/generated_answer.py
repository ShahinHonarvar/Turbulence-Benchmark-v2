def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_str = normalize(lst[i])
        if len(normalized_str) >= 3 and normalized_str not in anagram_set:
            anagram_set.add(normalized_str)
            for j in range(i + 1, len(lst)):
                if normalize(lst[j]) == normalized_str:
                    anagram_count += 1
                    if anagram_count > 78:
                        return False
    return True