def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[33:37]
    unique_numbers = list(set(numbers))
    number_counts = {num: numbers.count(num) for num in unique_numbers}
    sorted_unique_numbers = sorted(number_counts.keys(), reverse=True)
    if len(sorted_unique_numbers) < 2:
        return None
    else:
        second_largest = sorted_unique_numbers[1]
        if number_counts[second_largest] > 1:
            return second_largest
        else:
            for num in numbers:
                if num == second_largest:
                    return num
            return None