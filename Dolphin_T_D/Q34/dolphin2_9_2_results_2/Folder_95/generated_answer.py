def find_original_set(*args):
    output_set = set()
    for input_set in args:
        output_set = output_set.union(input_set)
    return output_set