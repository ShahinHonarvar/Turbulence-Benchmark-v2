def return_nth_smallest_ascii(s):
    Characters = sorted(s[:12], key=lambda x: ord(x))
    return Characters[11]