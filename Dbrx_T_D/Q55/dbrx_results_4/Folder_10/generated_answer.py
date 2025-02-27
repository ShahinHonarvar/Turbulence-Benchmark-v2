from itertools import islice, cycle

def sublists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst), i, i + len(lst)))
        for j in range(len(window)):
            if j == len(window) - 1 and window[0] * window[j] < n:
                window.extend(window[:j])
                if window[0] * window[len(window) // 2] == n:
                    result.append(window[:len(window) // 2 + 1])
                break
            elif window[0] * window[j] == n:
                result.append(window[:j + 1])
                break
    return result