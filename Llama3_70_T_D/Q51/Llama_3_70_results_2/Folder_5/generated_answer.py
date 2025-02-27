def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        lst[i] = ''.join(filter(str.isalpha, lst[i])).lower()
        for j in range(i + 1, len(lst)):
            lst[j] = ''.join(filter(str.isalpha, lst[j])).lower()
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i]) == sorted(lst[j])):
                anagrams_count += 1
    return anagrams_count <= 4