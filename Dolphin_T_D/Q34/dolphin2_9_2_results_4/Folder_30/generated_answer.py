def find_original_set(*args):
    sets = list(args)
    original_set = sets[0]
    for i in range(1, 78):
        for num in sets[i]:
            if num not in original_set:
                original_set.add(num)
    return original_set