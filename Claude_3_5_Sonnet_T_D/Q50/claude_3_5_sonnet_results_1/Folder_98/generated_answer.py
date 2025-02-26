def if_contains_anagrams(string_list):
    anagram_count = 0
    used_indices = set()
    for i in range(len(string_list)):
        if i in used_indices or len(string_list[i]) < 3:
            continue
        sorted_str = ''.join(sorted(string_list[i].lower()))
        for j in range(i + 1, len(string_list)):
            if j in used_indices or len(string_list[j]) < 3:
                continue
            if sorted_str == ''.join(sorted(string_list[j].lower())):
                anagram_count += 1
                used_indices.add(i)
                used_indices.add(j)
                if anagram_count >= 7:
                    return True
                break
    return False