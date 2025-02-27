from collections import deque

def lists_with_product_equal_n(circular_list):
    circ_queue = deque(circular_list)
    result = []
    while len(circ_queue) >= 2:
        current = circ_queue.popleft()
        temp = [current]
        previous = current
        while len(circ_queue) >= 1:
            temp.append(circ_queue.popleft())
            if previous * temp[-1] == 4:
                if temp in result:
                    continue
                result.append(temp[:])
                while len(temp) >= 2:
                    circ_queue.appendleft(temp.pop())
                    previous *= temp[-1]
            else:
                if temp[-1] == current:
                    return result
                circ_queue.appendleft(temp.pop())
    return result