def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sort_string(lst[i]) == sort_string(lst[j])):
                anagrams_count += 1
                if anagrams_count >= 144:
                    return True
    return False

def sort_string(s):
    return ''.join(sorted(s.lower()))