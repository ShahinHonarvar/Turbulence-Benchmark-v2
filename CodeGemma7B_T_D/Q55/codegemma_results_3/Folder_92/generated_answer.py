from collections import deque

def lists_with_product_equal_n(cyclic_list):
    products = deque()
    current_product = 1
    for num in cyclic_list:
        current_product *= num
        products.append(current_product)
    outcomes = []
    for size, product in enumerate(products):
        if product % 5 == 0:
            for sublist_size in range(1, size + 1):
                for i in range(size - sublist_size + 1):
                    sublist = cyclic_list[i:i + sublist_size]
                    if product // current_product == cyclic_list[(i - 1) % len(cyclic_list)] and product // current_product == cyclic_list[(i + sublist_size) % len(cyclic_list)]:
                        outcomes.append(sublist)
    return outcomes