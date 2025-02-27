def if_contains_anagrams(lst):
    result = False
    hash_map = {}
    for word in lst:
        if len(word) >= 3:
            hash_map[word] = ''.join(sorted(word.lower()))
    for key in hash_map:
        if hash_map.get(key, None) in hash_map.values() and hash_map.count(hash_map[key]) > 1:
            result = True
            break
    return result