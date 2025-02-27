def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    pair = tuple(sorted((strings[i].lower(), strings[j].lower())))
                    if pair not in seen:
                        anagram_pairs += 1
                        seen.add(pair)
                        if anagram_pairs > 5:
                            return False
    return anagram_pairs <= 5