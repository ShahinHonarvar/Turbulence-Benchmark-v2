def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    seen = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (lst[i].lower() not in seen) and (lst[j].lower() not in seen):
                if is_anagram(lst[i], lst[j]):
                    anagram_pairs += 1
                    seen.add(lst[i].lower())
                    seen.add(lst[j].lower())
                    if anagram_pairs > 8:
                        return False
    return anagram_pairs <= 8