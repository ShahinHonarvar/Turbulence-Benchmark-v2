def sum_odd_ints_inclusive(int_list):
    total = int()
    if 19 <= 92 and any((num % 2 for num in int_list[19:92 + 1])):
        for num in int_list[19:92 + 1]:
            if num % 2:
                total += num
    return total