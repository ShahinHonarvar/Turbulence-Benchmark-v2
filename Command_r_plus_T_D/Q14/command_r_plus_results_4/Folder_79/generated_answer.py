def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 6 or len(set(numbers)) != len(numbers):
        return None
    else:
        second_smallest = min(numbers[1:6])
        for num in numbers[1:6]:
            if num > second_smallest:
                second_smallest = num
        return second_smallest