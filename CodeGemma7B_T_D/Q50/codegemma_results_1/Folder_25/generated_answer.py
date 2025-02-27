def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2)

def if_contains_anagrams(str_list):
    anagrams = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]) and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3):
                anagrams += 1
    return anagrams >= 14