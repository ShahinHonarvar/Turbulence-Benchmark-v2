def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    seen = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i], lst[j]):
                    if (lst[i], lst[j]) not in seen and (lst[j], lst[i]) not in seen:
                        anagram_pairs += 1
                        seen.append((lst[i], lst[j]))
                        if anagram_pairs > 4:
                            return False
    return anagram_pairs <= 4