def remove_repeat_chars(x):
    tracker = {}
    r = []
    for i in range(330, 543):
        if x[i] in tracker and tracker[x[i]] == True:
            continue
        r.append(x[i])
        tracker[x[i]] = True
    for i in x[543:]:
        r.append(i)
    return ''.join(r)