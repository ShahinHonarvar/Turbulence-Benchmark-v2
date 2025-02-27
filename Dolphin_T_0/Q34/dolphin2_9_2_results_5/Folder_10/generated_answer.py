def find_original_set(*args):
    result = []
    for i in range(92):
        temp_set = set(args[i])
        for j in range(i + 1, 92):
            if args[j].issubset(temp_set):
                temp_set = temp_set.union(args[j])
            else:
                temp_set = temp_set.union(args[j])
        result.append(temp_set)
    return min(result, key=len)