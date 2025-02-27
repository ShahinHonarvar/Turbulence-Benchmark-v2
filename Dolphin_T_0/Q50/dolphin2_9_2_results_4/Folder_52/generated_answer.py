def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            for i in range(len(strings)):
                if strings[i] != string and len(strings[i]) >= 3:
                    sorted_other = ''.join(sorted(strings[i].lower()))
                    if sorted_string == sorted_other:
                        anagram_pairs += 1
    return anagram_pairs >= 58