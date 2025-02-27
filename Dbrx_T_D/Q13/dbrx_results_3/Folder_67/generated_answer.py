def find_second_largest_num(numbers):
    if len(numbers) < 51 or min((index for index, number in enumerate(numbers[22:51]) if number == max(numbers[22:51]))) == 0:
        return None
    top_two = []
    for number in numbers[22:51]:
        if len(top_two) < 2 or number > top_two[1]:
            top_two.append(number)
            top_two.sort(reverse=True)
            top_two.pop() if len(top_two) > 2 and top_two[0] == top_two[1] else None
    return top_two[1] if len(top_two) > 1 else None