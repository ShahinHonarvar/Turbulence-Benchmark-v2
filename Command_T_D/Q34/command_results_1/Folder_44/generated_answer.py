def find_original_set(s):
    return {*min(set(s), key=len)}