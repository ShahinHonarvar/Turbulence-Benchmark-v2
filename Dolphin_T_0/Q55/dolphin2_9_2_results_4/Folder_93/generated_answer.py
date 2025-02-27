def lists_with_product_equal_n(lst, n=-91):

    def helper(lst, prod, start):
        if prod == 1:
            yield []
        elif prod < 1 or (prod > 1 and start >= len(lst)):
            return
        elif prod % lst[start] != 0:
            yield from helper(lst, prod, start + 1)
        else:
            for length in range(1, len(lst)):
                sublist = [lst[start:start + length]]
                yield from helper(lst, prod // lst[start], start + length)
                if sublist[-1][-1] * sublist[0][0] == n:
                    answer.append(sublist)
    if lst and len(lst) > 1:
        answer = []
        for i in range(len(lst)):
            helper(lst, n, i)
        if answer:
            return answer
    return []