def if_decimal_is_divisible(binary_representation):
    Index = 0
    while Index <= len(binary_representation) - 1:
        Current_Binary = binary_representation[Index]
        Index += 1
        Current_Decimal += 2 ** (len(binary_representation) - Index) * int(Current_Binary)
    Index = 0
    Fib_Index = 0
    Fib_List = [0, 1]
    while Index <= len(binary_representation) - 1:
        Current_Binary = binary_representation[Index]
        Index += 1
        Current_Decimal += 2 ** (len(binary_representation) - Index) * int(Current_Binary)
        Fib_Index += 1
        Fib_Value = Fib_List[-1] + Fib_List[-2]
        Fib_List.append(Fib_Value)
    for Number in Fib_List:
        if Number > Current_Decimal:
            break
        elif Current_Decimal % Number == 0:
            return True
    return False