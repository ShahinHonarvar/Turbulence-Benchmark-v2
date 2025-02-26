def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        word1 = ''.join(sorted(filter(str.isalpha, string_list[i].lower())))
        if len(word1) < 3:
            continue
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            word2 = ''.join(sorted(filter(str.isalpha, string_list[j].lower())))
            if len(word2) < 3:
                continue
            if word1 == word2:
                anagram_count += 1
                processed.add(i)
                processed.add(j)
                if anagram_count > 5:
                    return False
                break
    return True