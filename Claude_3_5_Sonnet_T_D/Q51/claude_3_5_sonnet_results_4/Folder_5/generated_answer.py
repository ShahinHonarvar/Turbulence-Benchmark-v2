def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        current = ''.join(sorted(filter(str.isalpha, string_list[i].lower())))
        if len(current) < 3:
            continue
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            compare = ''.join(sorted(filter(str.isalpha, string_list[j].lower())))
            if len(compare) < 3:
                continue
            if current == compare:
                anagram_count += 1
                processed.add(j)
                if anagram_count > 4:
                    return False
                break
        processed.add(i)
    return True