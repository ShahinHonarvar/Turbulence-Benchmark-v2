def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if len(s1) < 3 or s1.lower() in processed:
            continue
        s1_sorted = ''.join(sorted(s1.lower()))
        for s2 in string_list[i + 1:]:
            if len(s2) < 3:
                continue
            if s1_sorted == ''.join(sorted(s2.lower())):
                anagram_count += 1
                processed.add(s1.lower())
                processed.add(s2.lower())
                if anagram_count >= 9:
                    return True
                break
    return False