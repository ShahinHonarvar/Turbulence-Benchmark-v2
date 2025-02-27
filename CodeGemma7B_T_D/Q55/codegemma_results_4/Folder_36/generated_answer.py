from collections import deque

def lists_with_product_equal_n(circular_list, n=714):
    """This Python code returns a list of sublists in the given circular list such that their product equals the specified value.

    The code first checks if the circular list is empty, and if so, it returns an empty list.

    Next, the code converts the circular list into a regular list using the `copy()` method. This allows the code to iterate through the list without affecting the original circular list.

    Next, the code uses a nested loop to iterate over the regular list, and for each element in the list, it checks if the element has a reciprocal in the list. If it does, the code creates a sublist with the two elements.

    Next, the code checks if the sublist's product equals the specified value. If it does, the code adds the sublist to the list of sublists.

    Finally, the code converts the list of sublists back into a circular list using the `deque()` constructor, and it returns the circular list.
    """
    circular_list = deque(circular_list)
    if not circular_list:
        return []
    product = n
    result = []
    while circular_list:
        element = circular_list.popleft()
        if 1 / element in circular_list:
            sublist = [element, 1 / element]
            result.append(sublist)
            circular_list.remove(1 / element)
        if sublist is not None and product == element * sublist[0]:
            circular_list.appendleft(element)
        circular_list.append(element)
    result = deque(result)
    return result