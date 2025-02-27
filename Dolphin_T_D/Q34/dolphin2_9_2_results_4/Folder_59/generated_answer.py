def find_original_set(*args):
    result = {}
    for i in range(len(args)):
        for num in args[i]:
            result[num] = result.get(num, 0) + 1
    return set((num for num, count in result.items() if count == len(args)))