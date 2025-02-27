from string import ascii_lowercase

def return_n_smallest_chars(str_param):
    str_param = str_param.lower()
    list_param = list(str_param)
    list_param.sort()
    return list_param[:58]