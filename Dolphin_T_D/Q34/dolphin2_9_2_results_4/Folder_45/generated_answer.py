def find_original_set(*args):
    result_set = set()
    for i in range(len(args)):
        if i == 0:
            result_set = args[i]
        else:
            for j in args[i]:
                if j not in result_set:
                    result_set.add(j)
    return result_set