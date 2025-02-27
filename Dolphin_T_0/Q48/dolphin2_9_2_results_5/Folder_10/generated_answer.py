def return_binary_or_hexa(numbers):
    a, b = (numbers[36], numbers[54])
    summ = sum(set(range(a + 1, b)) - set(numbers[36:55]))
    return bin(summ)[2:] if summ % 2 else hex(summ)[2:]