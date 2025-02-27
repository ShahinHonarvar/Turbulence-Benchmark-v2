def if_contains_anagrams(list1):
    count = 0
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    for i in list1:
        new_str = ''.join(sorted(i.lower()))
        if len(new_str) < 3:
            continue
        for j in list1:
            new_str1 = ''.join(sorted(j.lower()))
            if len(new_str1) < 3:
                continue
            if new_str == new_str1:
                count += 1
    if count >= 36:
        return True
    else:
        return False