def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    present_numbers = [num for num in numbers[10:13]]
    sum_nums = sum((num for num in range(a + 1, b) if num not in present_numbers))
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:] if sum_nums != 0 else ''