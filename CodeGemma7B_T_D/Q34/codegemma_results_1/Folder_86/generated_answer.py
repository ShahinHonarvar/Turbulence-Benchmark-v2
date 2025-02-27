def find_original_set(*args):
    args = list(*args)
    args.sort(key=len)
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            if args[j].issubset(args[i]):
                args.remove(args[j])
    return args[0]