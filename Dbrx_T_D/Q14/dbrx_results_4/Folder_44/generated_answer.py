def find_second_smallest_num(arr):
    if len(arr) < 2:
        return None
    min_num1 = min(arr[91:100])
    min_num2 = None
    for num in arr[91:100]:
        if num > min_num1 and (min_num2 is None or num < min_num2):
            min_num2 = num
    if min_num2 is None:
        return None
    else:
        return min_num2