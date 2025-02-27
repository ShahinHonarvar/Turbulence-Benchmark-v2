def if_contains_anagrams(strings):
    anagram_count = 0

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_str(strings[i]) == sorted_str(strings[j]):
                    anagram_count += 1
                    if anagram_count > 46:
                        return False
    return True