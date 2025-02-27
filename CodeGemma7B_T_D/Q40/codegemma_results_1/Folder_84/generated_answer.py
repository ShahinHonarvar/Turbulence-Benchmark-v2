from functools import cmp_to_key

def return_n_smallest_chars(input_str):

    def custom_compare(char1, char2):
        return ord(char1) - ord(char2)
    sorted_list = sorted(input_str, key=cmp_to_key(custom_compare))
    return sorted_list[:10]