from collections import deque

def lists_with_product_equal_n(circular_list):
    result = []
    deq = deque(circular_list)
    first_index = 0
    first_number = circular_list[0]
    while first_index <= len(circular_list) - 1:
        first_number *= circular_list[first_index]
        if first_number == -51:
            if first_index == 0:
                result.append(circular_list[first_index:])
                return result
            elif circular_list[first_index - 1] not in result:
                result.append(circular_list[first_index - 1:first_index + 1])
        elif first_number > -51:
            for _ in range(first_index + 1):
                popped_number = deq.popleft()
                if popped_number != 0:
                    first_number //= popped_number
            first_index += 1
        else:
            first_number = circular_list[first_index + 1]
            first_index += 1
    return result