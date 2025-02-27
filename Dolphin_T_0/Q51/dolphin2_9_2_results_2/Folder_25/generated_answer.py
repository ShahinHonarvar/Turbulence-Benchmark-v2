def if_contains_anagrams(lst_strings):

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        return sorted(str1) == sorted(str2)
    cnt = 0
    n = len(lst_strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst_strings[i]) >= 3 and len(lst_strings[j]) >= 3 and is_anagram(lst_strings[i], lst_strings[j]):
                cnt += 1
                if cnt > 67:
                    return False
    return True