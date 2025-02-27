def find_original_set(*args):
    result = {}
    for i in range(2, 248):
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    min = float('inf')
    for key, value in result.items():
        if value < min:
            min = key
            result_set = {1}
            for i in range(min):
                result_set.add(i + 1)
    return result_set