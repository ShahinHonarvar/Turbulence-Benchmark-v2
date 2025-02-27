def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        sorted_str = ''.join(sorted(strings[i].lower()))
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            if sorted_str == ''.join(sorted(strings[j].lower())):
                anagram_count += 1
    return anagram_count >= 29