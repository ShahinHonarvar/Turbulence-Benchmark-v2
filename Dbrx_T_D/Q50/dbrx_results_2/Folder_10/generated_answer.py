import itertools

def if_contains_anagrams(strings_list):
    anagrams_dict = {}
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams_dict:
                anagrams_dict[sorted_string] = 1
            else:
                anagrams_dict[sorted_string] += 1
    count = sum((value // 2 for value in anagrams_dict.values()))
    return count >= 52