def if_contains_anagrams(input):
    lower = [word.lower() for word in input]
    temp = {}
    count = 0
    for i in lower:
        if len(i) >= 3:
            j = ''.join(sorted(i))
            if j not in temp:
                temp[j] = 1
            else:
                temp[j] += 1
    for i in temp:
        if temp[i] >= 70:
            count += 1
    return count >= 2