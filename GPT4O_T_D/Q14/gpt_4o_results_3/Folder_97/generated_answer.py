def find_second_smallest_num(numbers):
    subarray = numbers[31:35]
    if len(subarray) < 2:
        return None
    first = second = float('inf')
    for num in subarray:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return second if second != float('inf') else None