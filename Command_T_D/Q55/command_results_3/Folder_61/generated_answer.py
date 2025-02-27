import heapq

def lists_with_product_equal_n(nums):
    result = []
    for x in nums:
        hq = []
        for i in range(1, x + 1):
            hq.append(x * i)
        hq.sort()
        hq.reverse()
        j = x - 1
        while hq and hq[0] == hq[-1]:
            hq.pop()
            j -= 1
        if hq:
            while hq[0] == hq[-1]:
                hq.pop()
            hq.sort()
            hq.reverse()
            heapq.heapify(hq)
            hq.append(hq[0])
            hq.sort()
            heapq.heapify(hq)
            while hq:
                y = heapq.heappop(hq)
                if y == x:
                    break
                elif y == x - 1:
                    y += 1
                elif y == x + 1:
                    y -= 1
                if hq:
                    heapq.heapify(hq)
                j = x - 1
                while hq and hq[0] == hq[-1]:
                    hq.pop()
                    j -= 1
                if hq:
                    heapq.heapify(hq)
                hq.append(hq[0])
                hq.sort()
                heapq.heapify(hq)
                while hq:
                    y = heapq.heappop(hq)
                    if y == x:
                        break
                    elif y == x - 1:
                        y += 1
                    elif y == x + 1:
                        y -= 1
                    if hq:
                        heapq.heapify(hq)
                    j = x - 1
                    while hq and hq[0] == hq[-1]:
                        hq.pop()
                        j -= 1
                    if hq:
                        heapq.heapify(hq)
                    hq.append(hq[0])
                    hq.sort()
                    heapq.heapify(hq)
                    while hq:
                        y = heapq.heappop(hq)
                        if y == x:
                            break
                        elif y == x - 1:
                            y += 1
                        elif y == x + 1:
                            y -= 1
                        if hq:
                            heapq.heapify(hq)
                        j = x - 1
                        while hq and hq[0] == hq[-1]:
                            hq.pop()
                            j -= 1
                        if hq:
                            heapq.heapify(hq)
                        hq.append(hq[0])
                        hq.sort()
                        heapq.heapify(hq)
                        while hq:
                            y = heapq.heappop(hq)
                            if y == x:
                                break
                            elif y == x - 1:
                                y += 1
                            elif y == x + 1:
                                y -= 1
                            if hq:
                                heapq.heapify(hq)
                            j = x - 1
                            while hq and hq[0] == hq[-1]:
                                hq.pop()
                                j -= 1
                            if hq:
                                heapq.heapify(hq)
                            hq.append(hq[0])
                            hq.sort()
                            heapq.heapify(hq)
                            while hq:
                                y = heapq.heappop(hq)
                                if y == x:
                                    break
                                elif y == x - 1:
                                    y += 1
                                elif y == x + 1:
                                    y -= 1
                                if hq:
                                    heapq.heapify(hq)
                                j = x - 1
                                while hq and hq[0] == hq[-1]:
                                    hq.pop()
                                    j -= 1
                                if hq:
                                    heapq.heapify(hq)
                                hq.append(hq[0])
                                hq.sort()
                                heapq.heapify(hq)
                                while hq:
                                    y = heapq.heappop(hq)
                                    if y == x:
                                        break
                                    elif y == x - 1:
                                        y += 1
                                    elif y == x + 1:
                                        y -= 1
                                    if hq:
                                        heapq.heapify(hq)
                                j = x - 1
                                while hq and hq[0] == hq[-1]:
                                    hq.pop()
                                    j -= 1
                                if hq:
                                    heapq.heapify(hq)
                                hq.append(hq[0])
                                hq.sort()
                                heapq.heapify(hq)
                                while hq:
                                    y = heapq.heappop(hq)
                                    if y == x:
                                        break
                                    elif y == x - 1:
                                        y += 1
                                    elif y == x + 1:
                                        y -= 1
                                    if hq:
                                        heapq.heapify(hq)
                                j = x - 1
                                while hq and hq[0] == hq[-1]:
                                    hq.pop()
                                    j -= 1
                                if hq:
                                    heapq.heapify(hq)
                                hq.append(hq[0])
                                hq.sort()
                                heapq.heapify(hq)
                                while hq:
                                    y = heapq.heappop(hq)
                                    if y == x:
                                        break
                                    elif y == x - 1:
                                        y += 1
                                    elif y == x + 1:
                                        y -= 1
                                    if hq:
                                        heapq.heapify(hq)
                                j = x - 1
                                while hq and hq[0] == hq[-1]:
                                    h