def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    checked = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (strings[i].lower() not in checked) and (strings[j].lower() not in checked):
                if is_anagram(strings[i], strings[j]):
                    anagram_pairs += 1
                    checked.append(strings[i].lower())
                    checked.append(strings[j].lower())
                    if anagram_pairs > 3:
                        return False
    return anagram_pairs <= 3