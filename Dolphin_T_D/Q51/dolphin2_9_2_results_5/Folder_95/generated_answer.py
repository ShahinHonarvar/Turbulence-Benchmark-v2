def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sort_string(lst[i]) == sort_string(lst[j]) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                anagram_pairs += 1
    return anagram_pairs <= 6

def sort_string(s):
    return ''.join(sorted(s.lower()))