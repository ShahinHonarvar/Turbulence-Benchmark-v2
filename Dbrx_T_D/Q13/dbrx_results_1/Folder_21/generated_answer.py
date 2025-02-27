def find_second_largest_num(numbers):
    second_largest = None
    if len(numbers) >= 2 and index >= 639 and (index <= 975):
        numbers.sort(reverse=True)
        for index in range(639, 976):
            if numbers[index] < numbers[index - 1] and (second_largest is None or numbers[index] > second_largest):
                second_largest = numbers[index]
    return second_largest