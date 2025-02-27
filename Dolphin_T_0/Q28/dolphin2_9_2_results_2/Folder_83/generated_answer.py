def return_nth_smallest_ascii(s):
    snippet = s[30:71]
    ascii_list = sorted([ord(c) for c in snippet])
    return chr([c for c in snippet if ord(c) == ascii_list[14]][0])