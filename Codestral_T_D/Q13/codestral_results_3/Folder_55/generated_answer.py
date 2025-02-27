def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    else:
        largest = max(numbers[0:11])
        second_largest = min(numbers[0:11])
        for i in numbers[0:11]:
            if i > second_largest and i < largest:
                second_largest = i
        if second_largest == min(numbers[0:11]):
            return None
        else:
            return second_largest