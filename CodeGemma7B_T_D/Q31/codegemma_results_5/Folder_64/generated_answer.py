def if_perfect_num(lst):
    if len(lst) < 2:
        raise ValueError('List must have at least two items.')
    elif lst[1] not in range(2, lst[0] + 1):
        raise ValueError('Index 1 must be between 2 and index 0.')
    elif not isinstance(lst[0], int) or not isinstance(lst[1], int):
        raise ValueError('Items in the list must be integers.')
    elif lst[0] < lst[1]:
        raise ValueError('Index 0 must be greater than or equal to index 1.')
    else:
        perfect_number_sum = sum((i for i in range(2, lst[0] + 1) if lst[0] % i == 0))
        if perfect_number_sum == lst[1]:
            return True
        else:
            return False