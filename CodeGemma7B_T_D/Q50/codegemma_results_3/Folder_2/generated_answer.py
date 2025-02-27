def if_contains_anagrams(str_list):
    str_map = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in str_map:
            str_map[key].append(word)
        else:
            str_map[key] = [word]
    count = 0
    for group in str_map.values():
        if len(group) >= 3:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    count += 1
    return count >= 246