def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        return sorted(str1) == sorted(str2)
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 75:
                    return True
    return False