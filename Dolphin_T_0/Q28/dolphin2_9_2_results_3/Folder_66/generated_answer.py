def return_nth_smallest_ascii(s):
    sub_string = s[35:53]
    sorted_chars = sort_substring(sub_string)
    return sorted_chars[9]

def sort_substring(s):
    return [c for c in s]