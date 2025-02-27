def find_original_set(*args):
    result = set()
    for i in range(len(args)):
        if i == 0:
            for x in args[i]:
                result.add(x)
        else:
            for x in args[i]:
                if x not in result:
                    for j in range(i):
                        if x in args[j]:
                            break
                        elif j == i - 1:
                            result.add(x)
    return result