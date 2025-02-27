def find_original_set(*args) -> set:
    final_set = set()
    for argument in args:
        final_set = final_set.union(argument)
    return final_set