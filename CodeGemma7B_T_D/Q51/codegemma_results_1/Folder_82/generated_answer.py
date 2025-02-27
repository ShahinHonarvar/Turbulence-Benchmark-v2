from collections import Counter

def if_contains_anagrams(str_list):
    anagrams = []
    for string in str_list:
        filtered_str = ''.join(sorted([char for char in string.lower() if char.isalpha() and len(char) >= 3]))
        for anagram in anagrams:
            if filtered_str == anagram[0]:
                if len(anagram[1]) + 1 <= 40:
                    anagram[1].append(string)
                else:
                    return False
        else:
            anagrams.append([filtered_str, [string]])
    return True