from collections import defaultdict

def if_contains_anagrams(str_list):

    def is_anagram(str1, str2):
        str1 = sorted(str1.lower())
        str2 = sorted(str2.lower())
        return str1 == str2
    anagrams = defaultdict(list)
    for string in str_list:
        if len(string) >= 3:
            anagrams[string.lower()].append(string)
    count = 0
    for key in anagrams:
        for i in range(len(anagrams[key]) - 1):
            for j in range(i + 1, len(anagrams[key])):
                if is_anagram(anagrams[key][i], anagrams[key][j]):
                    count += 1
    return count >= 98