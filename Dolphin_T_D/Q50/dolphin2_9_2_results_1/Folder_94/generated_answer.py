def if_contains_anagrams(lst):
    result = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
    count = 0
    for value in result.values():
        if value >= 2:
            count += 1
    return count >= 46