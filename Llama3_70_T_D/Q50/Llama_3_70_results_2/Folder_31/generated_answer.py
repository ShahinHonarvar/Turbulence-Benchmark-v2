def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i].lower()) >= 3 and sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagrams_count += 1
    return anagrams_count >= 68