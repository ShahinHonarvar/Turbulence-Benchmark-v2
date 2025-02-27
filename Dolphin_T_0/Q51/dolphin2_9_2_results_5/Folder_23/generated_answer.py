def if_contains_anagrams(lst):
    count = 0
    dic = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = ''.join(sorted(word))
        if key in dic:
            count += 1
            dic[key] += 1
        else:
            dic[key] = 1
    return count <= 49