def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            s1, s2 = (string_list[i], string_list[j])
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                anagram_pairs += 1
                processed.add(i)
                processed.add(j)
                if anagram_pairs > 2:
                    return False
                break
    return True