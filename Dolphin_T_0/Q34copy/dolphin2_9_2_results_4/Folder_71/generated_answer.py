def find_original_set(*args):
    final_set = set()
    for i in range(len(args)):
        if i == 0:
            final_set = args[i]
        else:
            final_set = final_set.union(args[i])
    return final_set