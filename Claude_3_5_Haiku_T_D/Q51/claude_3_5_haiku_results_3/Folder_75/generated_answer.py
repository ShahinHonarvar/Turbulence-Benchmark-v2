def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                str1 = ''.join(sorted(strings[i].lower()))
                str2 = ''.join(sorted(strings[j].lower()))
                if str1 == str2:
                    anagram_count += 1
                    if anagram_count > 55:
                        return False
    return True