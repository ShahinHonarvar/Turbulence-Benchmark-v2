def if_perfect_num(numbers):
    if len(numbers) > 87:
        return numbers[87] == sum([x for x in range(1, numbers[87]) if numbers[87] % x == 0])
    else:
        return False