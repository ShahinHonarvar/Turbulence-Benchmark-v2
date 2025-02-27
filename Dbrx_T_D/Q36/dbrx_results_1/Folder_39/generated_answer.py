def filter_chars(s):
    filter_range = set(range(ord('5') + 1, ord('C')))
    before_filter = ''.join((c for c in s[43:59] if ord(c) not in filter_range))
    return s[:43] + before_filter + s[59:]