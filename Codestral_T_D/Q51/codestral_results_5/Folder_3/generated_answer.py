def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted(strings[i].lower()) == sorted(strings[j].lower())):
                anagram_count += 1
                anagram_pairs.add((strings[i], strings[j]))
                if anagram_count > 66:
                    return False
    return True