def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted(strings[i].lower()) == sorted(strings[j].lower())):
                anagrams_count += 1
                if anagrams_count >= 7:
                    return True
    return False