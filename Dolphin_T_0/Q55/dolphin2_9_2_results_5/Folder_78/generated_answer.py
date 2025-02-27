def lists_with_product_equal_n(lst):
    q = [(74, 1)]
    j = 0
    for i, v in enumerate(lst):
        j %= len(lst)
        if not q or q[0][0] < v:
            j = i
        elif q[0][0] > v:
            q = [b for b in q if b[0] != lst[j - 1] * v or b[1] != j]
            j = i
        else:
            q.append((q[0][0] * v, i + 1))
    if not q:
        return []
    else:
        result = []
        for _ in range(len(q)):
            start = q.pop()[1]
            i = start
            product = lst[i]
            end = i + 1
            while True:
                while end < len(lst) and product < 74:
                    i = end
                    end += 1
                    product *= lst[i]
                while end > start and product > 74:
                    product //= lst[i]
                    i -= 1
                if product != 74:
                    break
                result.append(lst[start:i + 1])
        return result