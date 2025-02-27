def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = ''.join(sorted(strings[i].lower()))
            str2 = ''.join(sorted(strings[j].lower()))
            if len(str1) >= 3 and str1 == str2 and ((str1, str2) not in anagram_pairs):
                anagram_pairs.add((str1, str2))
                anagram_count += 1
                if anagram_count > 84:
                    return False
    return True