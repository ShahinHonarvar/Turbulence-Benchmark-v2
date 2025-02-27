def find_original_set(*args):
    result = set()
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            if args[i] < args[j]:
                result = args[i].union(args[j])
            else:
                result = args[j].union(args[i])
    return result