def if_contains_anagrams(strings):
    anagram_count = 0
    processed = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        sorted_str_1 = ''.join(sorted(strings[i].lower()))
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            sorted_str_2 = ''.join(sorted(strings[j].lower()))
            if sorted_str_1 == sorted_str_2:
                pair = (min(strings[i], strings[j]), max(strings[i], strings[j]))
                if pair not in processed:
                    anagram_count += 1
                    processed.add(pair)
                    if anagram_count > 26:
                        return False
    return True