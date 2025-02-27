def filter_chars(s):
    front_chars = s[:171]
    end_chars = s[636:]
    mid_chars = s[171:636]
    mid_chars = ''.join([c for c in mid_chars if c < 's' and c > 'c'])
    return front_chars + mid_chars + end_chars