import ctypes

def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) > 2 and len(string_list[j]) > 2 and set(string_list[i]).issubset(string_list[j]) and set(string_list[j]).issubset(string_list[i]) and (string_list[i].casefold() != string_list[j].casefold()):
                anagram_count += 1
    if anagram_count > 85:
        return False
    else:
        return True