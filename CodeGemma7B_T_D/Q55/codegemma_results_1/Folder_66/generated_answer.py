from collections import deque
from itertools import islice

def lists_with_product_equal_n(circlist):
    circular_deque = deque(circlist)
    sublists = []
    while circular_deque:
        sublist = []
        product = 1
        for i in range(len(circular_deque)):
            sublist.append(circular_deque.popleft())
            product *= circular_deque[-1]
            for a in range(len(circular_deque)):
                popped_element = circular_deque.popleft()
                if product // popped_element == sublist[-1]:
                    sublist.append(popped_element)
                    circular_deque.append(popped_element)
            if product != 78:
                for a in range(len(sublist)):
                    circular_deque.append(sublist.pop())
        if product == 78:
            sublists.append(sublist)
    return sublists