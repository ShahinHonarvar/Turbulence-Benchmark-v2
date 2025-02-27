def find_original_set(*sets):
    result = set()
    for i in range(63):
        for num in sets[i]:
            result.add(num)
    return result