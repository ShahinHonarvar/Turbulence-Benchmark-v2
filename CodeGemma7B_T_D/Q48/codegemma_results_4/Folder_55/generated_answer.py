def return_binary_or_hexa(numbers):
    nums = set(numbers[10:13])
    ans = sum((i for i in range(numbers[10] + 1, numbers[12]) if i not in nums))
    if ans % 2:
        return str(bin(ans))[2:]
    return hex(ans)[2:].upper() if numbers[10] % 2 else hex(ans)[2:].lower()