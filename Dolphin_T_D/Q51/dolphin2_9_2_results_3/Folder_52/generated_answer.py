def if_contains_anagrams(lst):
    count = 0
    hashmap = {}
    for word in lst:
        hashmap[word] = ''.join(sorted(word.lower()))
    for key, value in hashmap.items():
        if key not in hashmap.values() and len(key) >= 3:
            count += 1
    return count <= 43