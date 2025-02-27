def find_original_set(*args):
    final_set = set()
    for a in args:
        for num in a:
            final_set.add(num)
    return final_set