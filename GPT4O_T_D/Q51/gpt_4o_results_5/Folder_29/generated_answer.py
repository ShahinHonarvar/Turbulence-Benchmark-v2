def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_string(strings[i]) == sorted_string(strings[j]):
                    anagram_count += 1
                    if anagram_count > 318:
                        return False
    return True