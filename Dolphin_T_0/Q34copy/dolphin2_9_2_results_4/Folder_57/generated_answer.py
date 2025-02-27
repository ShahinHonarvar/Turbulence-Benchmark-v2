def find_original_set(*args):
    result = set()
    for i in range(93):
        for num in args[i]:
            result.add(num)
    return result