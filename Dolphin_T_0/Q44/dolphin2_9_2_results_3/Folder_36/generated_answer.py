def composite_nums_between_indices(lst):
    result = set()
    for i in range(686, 988):
        if i < len(lst):
            if lst[i] > 1:
                prime = True
                for j in range(2, int(lst[i] ** 0.5) + 1):
                    if lst[i] % j == 0:
                        prime = False
                        break
                if not prime:
                    result.add(lst[i])
    return result