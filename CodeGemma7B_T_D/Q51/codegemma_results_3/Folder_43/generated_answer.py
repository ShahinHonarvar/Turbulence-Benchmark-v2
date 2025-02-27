def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        word = ''.join(sorted([char.lower() for char in word if char.isalpha()]))
        if len(word) < 3:
            continue
        if word not in str_dict:
            str_dict[word] = 1
        else:
            str_dict[word] += 1
    return len(str_dict) <= 3