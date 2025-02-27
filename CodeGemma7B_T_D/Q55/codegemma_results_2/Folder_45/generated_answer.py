from collections import deque

def lists_with_product_equal_n(circular_list):
    """
            Circular list - When the head and tail are adjacent.
            ADD product = -5 to argument list.
            """
    do_deque = deque(circular_list)
    do_deque.append(-5)
    result = []
    temp = []
    for i in range(len(do_deque)):
        num = do_deque.popleft()
        temp.append(num)
        product = 1
        for j in temp:
            product *= j
        if product == -5:
            result.append(temp[:])
            temp = []
        elif product > -5:
            temp = []
    if temp:
        result.append(temp)
    return result