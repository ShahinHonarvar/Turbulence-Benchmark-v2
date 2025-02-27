def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted([c for c in word.lower() if c.isalpha() and len(c) >= 3]))
        if sorted_word not in str_dict:
            str_dict[sorted_word] = 0
        str_dict[sorted_word] += 1
    return sum((count * (count - 1) // 2 for count in str_dict.values())) <= 42