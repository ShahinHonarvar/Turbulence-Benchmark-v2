def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    tuple_sum = sum(numbers[933:997])
    total_sum = sum(range(a + 1, b))
    result = total_sum - tuple_sum
    if result == 0:
        return ''
    if result % 2 != 0:
        return bin(result)[2:]
    return hex(result)[2:]