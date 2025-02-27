from collections import Counter

def if_contains_anagrams(lst_strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    num_anagrams = 0
    n = len(lst_strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst_strings[i]) == len(lst_strings[j]) >= 3 and is_anagram(lst_strings[i], lst_strings[j]):
                num_anagrams += 1
    num_max_anagrams = n * (n - 1) // 2
    return num_anagrams <= num_max_anagrams // 36