def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = normalize_string(lst[i])
            str2 = normalize_string(lst[j])
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pair = tuple(sorted((lst[i], lst[j])))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 318:
                        return False
    return True