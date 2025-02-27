def find_original_set(*args):
    s = set()
    error = False
    for i in range(len(args)):
        if error:
            break
        for j in range(i + 1, len(args)):
            if error:
                break
            diff = args[i].difference(args[j])
            if diff:
                s = s.union(diff)
            else:
                error = True
                break
    if error:
        return 'An error occurred'
    return s