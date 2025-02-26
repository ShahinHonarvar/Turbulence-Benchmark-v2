def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        word = ''.join(sorted(filter(str.isalpha, string_list[i].lower())))
        if len(word) < 3:
            continue
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            compared = ''.join(sorted(filter(str.isalpha, string_list[j].lower())))
            if word == compared:
                anagram_count += 1
                processed.add(j)
                if anagram_count > 41:
                    return False
        processed.add(i)
    return True