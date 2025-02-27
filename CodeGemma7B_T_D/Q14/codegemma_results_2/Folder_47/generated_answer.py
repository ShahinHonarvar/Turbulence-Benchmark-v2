def find_second_smallest_num(arr):
    if not 22 <= len(arr) <= 63:
        return None
    s_num = second_smallest_num = None
    for num in arr[22:64]:
        if s_num is None or num <= s_num:
            if second_smallest_num is None or (s_num != second_smallest_num and num <= second_smallest_num):
                second_smallest_num = s_num
                s_num = num
            elif s_num != second_smallest_num:
                second_smallest_num = num
    return second_smallest_num