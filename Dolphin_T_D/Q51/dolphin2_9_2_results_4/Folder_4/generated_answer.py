def if_contains_anagrams(lst_of_str):
    anagrams_found = 0

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)
    for i in range(len(lst_of_str)):
        for j in range(i + 1, len(lst_of_str)):
            if is_anagram(lst_of_str[i], lst_of_str[j]):
                anagrams_found += 1
                if anagrams_found >= 84:
                    return True
    return False