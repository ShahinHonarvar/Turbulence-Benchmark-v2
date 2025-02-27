def return_nth_smallest_ascii(input_string):
    if len(input_string) < 4:
        return None
    else:
        substring = input_string[:4]
        sorted_substring = sorted(substring)
        return sorted_substring[3]