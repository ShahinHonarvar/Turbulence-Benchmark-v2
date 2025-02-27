def if_contains_anagrams(lst):
    count = 0
    hash_map = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hash_map:
                hash_map[word] = 1
            else:
                count += 1
    return count <= 46