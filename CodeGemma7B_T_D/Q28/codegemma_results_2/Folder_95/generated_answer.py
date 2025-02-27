def return_nth_smallest_ascii(str):
    return min((str[i] for i in range(1, 47) if str[i] != str[0]))