def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        str1 = ''.join(sorted(strings[i].lower()))
        if len(strings[i]) >= 3:
            for j in range(i + 1, len(strings)):
                str2 = ''.join(sorted(strings[j].lower()))
                if str1 == str2:
                    anagram_count += 1
                    if anagram_count >= 123:
                        return True
    return False