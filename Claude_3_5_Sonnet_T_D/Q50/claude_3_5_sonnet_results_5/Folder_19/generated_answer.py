def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed or len(string_list[i]) < 3:
            continue
        current = string_list[i].lower()
        sorted_current = ''.join(sorted(current))
        for j in range(i + 1, len(string_list)):
            if j in processed or len(string_list[j]) < 3:
                continue
            compare = string_list[j].lower()
            if len(current) == len(compare) and sorted_current == ''.join(sorted(compare)):
                anagram_count += 1
                processed.add(j)
                if anagram_count >= 84:
                    return True
    return False