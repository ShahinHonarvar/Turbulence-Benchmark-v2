def if_contains_anagrams(strings):
    if len(strings) < 6:
        return False
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_count += 1
                    break
    return anagram_count >= 3