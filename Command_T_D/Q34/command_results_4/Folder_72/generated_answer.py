def find_original_set(s):
    return {i for i in range(min(s), max(s) + 1) if not s & {i}}