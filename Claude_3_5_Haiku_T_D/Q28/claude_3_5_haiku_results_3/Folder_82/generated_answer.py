def return_nth_smallest_ascii(string):
    if len(string) < 15:
        return min(string)
    substring = string[:15]
    sorted_substring = sorted(substring)
    return sorted_substring[14]