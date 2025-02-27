def if_contains_anagrams(str_list):
    found_anagrams = 0
    str_dict = {}
    for text in str_list:
        sorted_text = ''.join(sorted(text.lower()))
        if sorted_text not in str_dict:
            str_dict[sorted_text] = [text]
        else:
            str_dict[sorted_text].append(text)
    for text_count in str_dict.values():
        if len(text_count) >= 3:
            found_anagrams += 1
        if found_anagrams >= 3:
            return True
    return False