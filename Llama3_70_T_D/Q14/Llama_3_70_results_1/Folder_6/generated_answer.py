def find_second_smallest_num(numbers):
    if len(numbers) < 80:
        return None
    else:
        smallest = min(numbers[29:80])
        second_smallest = min((i for i in numbers[29:80] if i != smallest))
        if second_smallest == smallest:
            return None
        else:
            return second_smallest