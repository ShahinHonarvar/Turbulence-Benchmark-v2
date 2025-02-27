from itertools import islice
from collections import deque

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        window = deque(maxlen=i + 1)
        product = 1
        for j in range(i, len(numbers)):
            window.append(numbers[j])
            product *= numbers[j]
            if product == 5:
                result.append(list(window))
            while product > 5 and window:
                product //= window.popleft()
    return result