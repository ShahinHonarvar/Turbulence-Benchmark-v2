def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list.sort(key=len)
    anagram_count = 0
    curr_str = str_list[0]
    curr_str_len = len(curr_str)
    for i in range(1, len(str_list)):
        if len(str_list[i]) <= curr_str_len:
            continue
        str_sorted = sorted(str_list[i])
        curr_str_sorted = sorted(curr_str)
        if str_sorted == curr_str_sorted:
            anagram_count += 1
            if anagram_count >= 48:
                return True
        curr_str = str_list[i]
        curr_str_len = len(curr_str)
    return False