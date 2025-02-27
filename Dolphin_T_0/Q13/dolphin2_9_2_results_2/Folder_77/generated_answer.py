def find_second_largest_num(arr):
    if len(arr[527:538]) < 2:
        return None
    first = second = -float('inf')
    for i in arr[527:538]:
        if i > first:
            first, second = (i, first)
        elif i > second and i != first:
            second = i
    return second