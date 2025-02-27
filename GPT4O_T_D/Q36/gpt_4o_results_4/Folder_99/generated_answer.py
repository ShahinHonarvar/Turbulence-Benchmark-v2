def filter_deletion_list(s):
    return ''.join((c for c in set(s) if 'b' < c < 'd'))

def filter_chars(s):
    deletion_list = filter_deletion_list(s[477:948])
    return ''.join((c for c in s if c not in deletion_list))