def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        current = string_list[i].lower()
        if len(current) < 3:
            continue
        sorted_current = ''.join(sorted(current))
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            compare = string_list[j].lower()
            if len(compare) < 3:
                continue
            if sorted_current == ''.join(sorted(compare)):
                anagram_count += 1
                processed.add(j)
                if anagram_count >= 140:
                    return True
        processed.add(i)
    return False