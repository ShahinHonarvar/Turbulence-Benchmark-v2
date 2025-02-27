def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list if len(s) >= 3]

    def is_anagram(s1, s2):
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        return sorted_s1 == sorted_s2
    count = len(str_list)
    for i in range(count):
        for j in range(i + 1, count):
            if is_anagram(str_list[i], str_list[j]):
                count -= 1
                if count <= 122:
                    return True
    return False