def all_odd_ints_exclusive(odd_list):
    result = []
    for num in odd_list[78:93]:
        if num % 2 != 0:
            result.append(num)
    if not result:
        return []
    return result