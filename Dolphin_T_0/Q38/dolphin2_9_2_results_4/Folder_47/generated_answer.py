def find_subset_of_length_n(s):
    if len(s) < 34:
        return 0
    else:
        x = len(s)
        ans = 0
        for i in range(1 << x):
            y = bin(i)[2:]
            y = y.zfill(x)
            count = 0
            for j in y:
                if j == '1':
                    count += 1
            if count == 34:
                ans += 1
        return ans