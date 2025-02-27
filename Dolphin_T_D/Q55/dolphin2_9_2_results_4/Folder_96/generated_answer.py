def lists_with_product_equal_n(a_list):
    result = []
    head = 0
    tail = 0
    total = 1
    while tail < len(a_list):
        total = total * a_list[tail]
        if total == 0:
            result.append(a_list[head:tail + 1])
            head = tail + 1
        if tail + 1 == len(a_list) and head != tail + 1:
            total = total // a_list[head]
            head = head + 1
            tail = head
            total = 1
        tail = tail + 1
    if len(result) == 0:
        return []
    else:
        return result