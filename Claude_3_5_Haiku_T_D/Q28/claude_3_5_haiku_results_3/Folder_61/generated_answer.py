def return_nth_smallest_ascii(string):
    if len(string) < 10:
        return min(string)
    return sorted(string[:10])[9]