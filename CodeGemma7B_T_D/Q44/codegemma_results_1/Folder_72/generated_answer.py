def composite_nums_between_indices(num):
    a = num[55:99]
    composite = set()
    for i in a:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if not prime:
            composite.add(i)
    return composite