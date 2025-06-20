def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_str = normalize(lst[i])
        if len(normalized_str) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if normalize(lst[j]) == normalized_str:
                pair = tuple(sorted((lst[i], lst[j])))
                if pair not in anagram_set:
                    anagram_set.add(pair)
                    anagram_count += 1
                    if anagram_count > 73:
                        return False
    return True