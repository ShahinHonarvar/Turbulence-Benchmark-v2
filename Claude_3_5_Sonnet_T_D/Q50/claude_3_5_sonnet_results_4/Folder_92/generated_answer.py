def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed or len(string_list[i]) < 3:
            continue
        current = ''.join(sorted(string_list[i].lower()))
        for j in range(i + 1, len(string_list)):
            if j in processed or len(string_list[j]) < 3:
                continue
            comparison = ''.join(sorted(string_list[j].lower()))
            if current == comparison:
                anagram_count += 1
                processed.add(i)
                processed.add(j)
                if anagram_count >= 2:
                    return True
                break
    return False