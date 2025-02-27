def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(set(strings[i].lower()) & set(strings[j].lower())) >= 3 and sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagram_count += 1
    return anagram_count >= 78