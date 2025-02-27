def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if set(strings[i].lower()) == set(strings[j].lower()) and len(strings[i]) >= 3:
                sorted_i = sorted(strings[i].lower())
                sorted_j = sorted(strings[j].lower())
                if sorted_i == sorted_j:
                    anagrams_count += 1
    return anagrams_count <= 69