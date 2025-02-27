def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [s.lower() for s in lst if s.isalpha() and len(s) >= 3]
    lst.sort()
    i = 0
    while i < len(lst):
        count = 1
        j = i + 1
        while j < len(lst) and sorted(lst[i]) == sorted(lst[j]):
            j += 1
            count += 1
        anagrams_count += count * (count - 1) // 2
        i = j
        if anagrams_count > 50:
            return False
    return True