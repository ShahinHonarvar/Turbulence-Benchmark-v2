def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list.sort(key=len)
    pairs = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                pairs += 1
            if pairs >= 39:
                return False
    return True