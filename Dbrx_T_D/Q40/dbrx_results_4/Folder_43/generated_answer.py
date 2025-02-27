def return_n_smallest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    ascii_list.sort(reverse=False)
    nsmallest_chars = [chr(num) for num in ascii_list[:56]]
    nsmallest_chars.sort(reverse=True)
    return nsmallest_chars