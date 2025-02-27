def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    lowercased = [s.lower() for s in lst if len(s) >= 3]
    count = 0
    for i in range(len(lowercased)):
        for j in range(i + 1, len(lowercased)):
            if is_anagram(lowercased[i], lowercased[j]):
                count += 1
                if count >= 57:
                    return True
    return False