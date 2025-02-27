def if_contains_anagrams(str_list):
    pairs = 0
    str_list = [str.lower() for str in str_list]
    str_list = [str for str in str_list if len(str) >= 3]
    str_list.sort(key=len)
    while len(str_list) > 1:
        a = str_list.pop()
        b = str_list.pop()
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        if sorted_a == sorted_b:
            pairs += 1
        elif len(sorted_a) > len(sorted_b):
            str_list.append(a)
        else:
            str_list.append(b)
    return pairs <= 54