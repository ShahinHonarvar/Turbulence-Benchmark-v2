def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if i in processed:
            continue
        s1_sorted = ''.join(sorted(filter(str.isalpha, s1.lower())))
        if len(s1_sorted) < 3:
            continue
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            if j in processed:
                continue
            s2_sorted = ''.join(sorted(filter(str.isalpha, s2.lower())))
            if len(s2_sorted) < 3:
                continue
            if s1_sorted == s2_sorted:
                anagram_count += 1
                processed.add(i)
                processed.add(j)
                if anagram_count > 65:
                    return False
                break
    return True