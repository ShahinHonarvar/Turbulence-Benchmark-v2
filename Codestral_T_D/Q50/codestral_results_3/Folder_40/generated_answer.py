def if_contains_anagrams(strings):
    anagram_count = 0
    checked = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and sorted(strings[i].lower()) == sorted(strings[j].lower()) and (strings[i].lower() not in checked) and (strings[j].lower() not in checked):
                anagram_count += 1
                checked.add(strings[i].lower())
                checked.add(strings[j].lower())
                if anagram_count >= 3:
                    return True
    return False