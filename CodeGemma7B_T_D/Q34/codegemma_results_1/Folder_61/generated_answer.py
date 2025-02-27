def find_original_set(set_a, set_b, set_c, set_d):
    result = set()
    for element in set_a:
        if element not in result:
            result.add(element)
    for element in set_b:
        if element not in result:
            result.add(element)
    for element in set_c:
        if element not in result:
            result.add(element)
    for element in set_d:
        if element not in result:
            result.add(element)
    return result