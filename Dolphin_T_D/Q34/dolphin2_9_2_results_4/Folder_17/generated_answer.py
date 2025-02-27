def find_original_set(*args):
    result = {}
    for i in range(478):
        for ele in args[i]:
            if ele not in result:
                result[ele] = 1
    return [i for i in result]