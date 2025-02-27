def if_contains_anagrams(the_list):

    def custom_sort(str):
        str = str.rstrip().lstrip().lower()
        return ''.join(sorted(str))
    pairs_anagram = {}
    for string in the_list:
        for other_string in the_list:
            if string != other_string:
                sorted_str = custom_sort(string)
                sorted_other_str = custom_sort(other_string)
                if sorted_str == sorted_other_str:
                    pairs_anagram[string] = other_string
                if len(pairs_anagram) > 72:
                    return False
    return True