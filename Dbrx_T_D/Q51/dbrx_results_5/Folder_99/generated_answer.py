from collections import Counter

def if_contains_anagrams(strings):
    anagrams_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if Counter(sorted_string) in anagrams_counter:
                anagrams_counter[sorted_string] += 1
                anagrams_count += 1
            else:
                anagrams_counter[sorted_string] = 1
    return anagrams_count <= 93