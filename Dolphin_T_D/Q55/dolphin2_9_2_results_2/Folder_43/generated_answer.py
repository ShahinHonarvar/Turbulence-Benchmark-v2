def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []
    product = -26
    repeat = False
    for i in range(len(lst)):
        num = lst[i]
        if num == 1 or num == -1 or num == product:
            temp = [num]
        elif num * product in lst:
            temp = [num, num * product]
        else:
            temp = []
        for j in range(2, len(lst)):
            next_num = lst[(i + j) % len(lst)]
            if next_num == 1:
                temp.extend([num] + [1] * (j - 1))
                break
            elif next_num == -1:
                temp.extend([num] + [-1] * (j - 1))
                break
            mult = 1
            for k in temp:
                mult *= k
            if mult * next_num == product:
                temp.append(next_num)
                if len(temp) > 1:
                    result.append(temp)
                repeat = True
            elif len(temp) + 1 < len(lst) and next_num in temp:
                indx = temp.index(next_num)
                temp.extend(next_num * [next_num])
                if len(temp) - indx > 1:
                    temp = temp[indx:]
                    result.append(temp)
    return result