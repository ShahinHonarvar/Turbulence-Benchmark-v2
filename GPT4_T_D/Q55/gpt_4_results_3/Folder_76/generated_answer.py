from collections import deque

def lists_with_product_equal_n(circ_list):
    circ_queue = deque(circ_list)
    result = []
    for _ in range(len(circ_queue)):
        for i in range(1, len(circ_queue) + 1):
            sublist = list(circ_queue)[:i]
            mult = 1
            for n in sublist:
                mult *= n
            if mult == 247:
                result.append(sublist)
        circ_queue.rotate(-1)
    return result