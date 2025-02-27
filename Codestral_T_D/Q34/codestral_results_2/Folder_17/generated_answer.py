def find_original_set(s1, s2, s3, *args):
    original_set = set.union(*args)
    original_set.update(s1, s2, s3)
    return original_set